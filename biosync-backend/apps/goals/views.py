from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.goals.models import Goal
from apps.goals.serializers import GoalSerializer
from apps.core.permissions import IsOwner # Reusing the custom permission class

class GoalViewSet(viewsets.ModelViewSet):
    """
    API endpoints for managing user fitness goals (CRUD operations).
    """
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    
    # Allows filtering goals by status or type
    filterset_fields = ['status', 'goal_type']
    
    # Allows ordering results by date fields
    ordering_fields = ['start_date', 'target_date', 'created_at']
    ordering = ['-created_at'] # Default: show newest goals first

    def get_queryset(self):
        """ Filters the queryset to only return goals owned by the current user. """
        if self.request.user.is_authenticated:
            return Goal.objects.filter(user=self.request.user)
        return Goal.objects.none()

    def perform_create(self, serializer):
        """ Sets the user field to the current authenticated user upon creation. """
        serializer.save(user=self.request.user)
        
    # No custom actions are required here yet, but could be added for goal progress tracking.
