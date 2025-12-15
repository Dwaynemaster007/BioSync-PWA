from rest_framework import serializers
from .models import ProgressEntry
from apps.goals.models import Goal
from django.db import transaction

class ProgressEntrySerializer(serializers.ModelSerializer):
    # Read-only field to show the goal's title in the entry response
    goal_title = serializers.CharField(source='goal.title', read_only=True)
    
    class Meta:
        model = ProgressEntry
        fields = (
            'id', 'user', 'goal', 'goal_title', 'date', 'value', 'notes', 
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'user', 'created_at', 'updated_at', 'goal_title')

    def create(self, validated_data):
        # Use a transaction to ensure both the entry creation and goal update succeed or fail together.
        with transaction.atomic():
            # 1. Create the ProgressEntry
            progress_entry = ProgressEntry.objects.create(**validated_data)
            
            # 2. Update the Goal's current_value
            goal = progress_entry.goal
            
            # The Goal model's current_value field is a DecimalField
            new_value = goal.current_value + progress_entry.value

            # Update the status if the goal is completed
            new_status = goal.status
            if new_value >= goal.target_value:
                new_status = 'COMPLETED'
            elif goal.status == 'NOT_STARTED' and new_value > 0:
                new_status = 'IN_PROGRESS'
            # If it was already IN_PROGRESS, it remains IN_PROGRESS unless COMPLETED

            goal.current_value = new_value
            goal.status = new_status
            goal.save(update_fields=['current_value', 'status', 'updated_at'])
            
            return progress_entry
