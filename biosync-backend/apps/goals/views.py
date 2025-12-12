from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Goal
from .serializers import GoalSerializer

class GoalViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Goal instances.
    Requires authentication to list, retrieve, create, update, or destroy goals.
    Goals are automatically filtered by the authenticated user.
    """
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Restricts the queryset to only goals belonging to the current user.
        """
        return Goal.objects.filter(user=self.request.user).order_by('-target_date', 'status')

    def perform_create(self, serializer):
        """
        Injects the authenticated user into the Goal object before saving.
        """
        serializer.save(user=self.request.user)

    # Example of a custom action: Mark goal as completed
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """Marks a goal as COMPLETED and sets current_value to target_value."""
        goal = self.get_object()
        goal.status = 'COMPLETED'
        goal.current_value = goal.target_value # Ensure 100% completion
        goal.save()
        return Response({'status': 'goal marked as completed', 'current_value': goal.current_value})
