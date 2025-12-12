from rest_framework import serializers
from apps.goals.models import Goal

class GoalSerializer(serializers.ModelSerializer):
    """
    Serializer for the Goal model.
    """
    # Read-only field for the user email/username for easy display
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Goal
        fields = [
            'id', 'user', 'goal_type', 'title', 'description', 
            'target_value', 'target_unit', 'wger_exercise_id', 
            'start_date', 'target_date', 'status', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
