from rest_framework import viewsets, permissions
from .models import ProgressEntry
from .serializers import ProgressEntrySerializer
from rest_framework.exceptions import ValidationError
from django.db.models import Q

class ProgressEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for detailed Progress Entries.
    Allows listing, creating, retrieving, updating, and destroying progress records.
    """
    serializer_class = ProgressEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensures users only see their own progress entries.
        Optionally allows filtering by 'goal_id' in the URL query.
        """
        queryset = ProgressEntry.objects.filter(user=self.request.user)
        
        goal_id = self.request.query_params.get('goal_id')
        if goal_id is not None:
            # Filter entries specifically for a given goal
            queryset = queryset.filter(goal__id=goal_id)
            
        return queryset.select_related('goal').order_by('-date')

    def perform_create(self, serializer):
        # Automatically set the user before saving
        serializer.save(user=self.request.user)
        
        # Note: The logic to update the Goal's current_value is now handled in the Serializer's create method.

    def perform_destroy(self, instance):
        """
        Custom delete logic to rollback the progress on the associated Goal.
        """
        goal = instance.goal
        
        # Rollback the current_value
        goal.current_value -= instance.value
        if goal.current_value < 0:
            goal.current_value = 0 # Prevent negative progress
            
        # Recalculate status based on new value
        if goal.current_value == 0:
            goal.status = 'NOT_STARTED'
        elif goal.current_value < goal.target_value:
            goal.status = 'IN_PROGRESS'
        # If it was previously 'COMPLETED' and is now below the target, set back to 'IN_PROGRESS'
        elif goal.current_value < goal.target_value and goal.status == 'COMPLETED':
            goal.status = 'IN_PROGRESS'

        goal.save(update_fields=['current_value', 'status', 'updated_at'])
        
        instance.delete()
        
    def perform_update(self, serializer):
        """
        Disallow simple updates (PUT/PATCH) for now to prevent complex calculation errors.
        The user should delete the entry and create a new one to ensure goal history remains linear.
        """
        raise ValidationError("Directly updating progress entries is not allowed. Please delete the entry and log a new one for accurate history.")
