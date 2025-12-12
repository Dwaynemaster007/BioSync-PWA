from rest_framework import serializers
from .models import Workout, ExerciseLog, SetLog, BiometricData

# --- SetLog Serializer (Innermost Tier) ---

class SetLogSerializer(serializers.ModelSerializer):
    """Serializer for the granular SetLog model."""
    class Meta:
        model = SetLog
        # Exclude 'exercise_log' field here as it is handled by the parent serializer
        fields = ('id', 'set_number', 'weight_kg', 'repetitions', 'rpe', 'to_failure', 'created_at')
        read_only_fields = ('id', 'created_at')


# --- ExerciseLog Serializer (Middle Tier) ---

class ExerciseLogSerializer(serializers.ModelSerializer):
    """
    Serializer for the ExerciseLog model.
    It includes nested SetLogSerializer to handle sets within an exercise.
    """
    sets = SetLogSerializer(many=True) # Nested field for the related SetLog objects

    class Meta:
        model = ExerciseLog
        # Exclude 'workout' field here as it is handled by the parent serializer
        fields = ('id', 'wger_exercise_id', 'custom_name', 'order_in_workout', 'sets', 'created_at')
        read_only_fields = ('id', 'created_at')


# --- Workout Serializer (Top Tier) ---

class WorkoutSerializer(serializers.ModelSerializer):
    """
    Serializer for the main Workout model.
    It includes nested ExerciseLogSerializer to handle the entire workout structure.
    """
    exercises = ExerciseLogSerializer(many=True) # Nested field for the related ExerciseLog objects
    
    # Ensure the user field is read-only and defaults to the current authenticated user
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Workout
        fields = (
            'id', 'user', 'title', 'start_time', 'end_time', 
            'duration_minutes', 'activity_type', 'notes', 
            'exercises', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

    def create(self, validated_data):
        """
        Handles the creation of a Workout and all nested ExerciseLog and SetLog instances.
        """
        # 1. Pop nested data
        exercises_data = validated_data.pop('exercises')
        
        # 2. Create the top-level Workout instance
        # Add the request user to the validated data before creating the workout
        user = self.context['request'].user
        workout = Workout.objects.create(user=user, **validated_data)

        # 3. Iterate through exercises
        for exercise_data in exercises_data:
            sets_data = exercise_data.pop('sets')
            
            # Create the ExerciseLog instance
            exercise_log = ExerciseLog.objects.create(workout=workout, **exercise_data)

            # 4. Iterate through sets
            set_logs = [
                SetLog(exercise_log=exercise_log, **set_data)
                for set_data in sets_data
            ]
            # Bulk create all sets for efficiency
            SetLog.objects.bulk_create(set_logs)

        return workout

    # NOTE: Update method would be complex due to nested data, 
    # and is often handled by separate PUT/PATCH endpoints for individual nested resources (sets/exercises).
    # For simplicity, we are currently only implementing deep creation.

# --- Biometric Data Serializer ---

class BiometricDataSerializer(serializers.ModelSerializer):
    """Serializer for BiometricData model."""
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = BiometricData
        fields = (
            'id', 'user', 'timestamp', 'recorded_weight_kg', 
            'sleep_duration_hours', 'sleep_score', 
            'resting_heart_rate', 'heart_rate_variability', 
            'readiness_score', 'created_at'
        )
        read_only_fields = ('id', 'user', 'created_at')
