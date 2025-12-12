from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    # Read-only field for progress percentage, calculated in the model
    progress_percentage = serializers.ReadOnlyField()

    class Meta:
        model = Goal
        fields = [
            'id', 
            'user', 
            'title', 
            'description', 
            'start_date', 
            'target_date', 
            'target_value', 
            'target_unit', 
            'current_value',  # New field added for progress tracking
            'status', 
            'goal_type', 
            'created_at', 
            'updated_at', 
            'progress_percentage'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at', 'progress_percentage']
        # The 'user' field will be automatically set in the view to the authenticated user

    def create(self, validated_data):
        # We need to explicitly handle the user field since it's read_only in Meta but required for creation
        # The view (GoalViewSet) is responsible for injecting the user during creation.
        # This serializer remains clean for standard model operations.
        return Goal.objects.create(**validated_data)
