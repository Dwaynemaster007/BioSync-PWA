from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, F

from .models import Workout, BiometricData
from .serializers import WorkoutSerializer, BiometricDataSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Workout instances.
    Handles nested creation (Workout -> ExerciseLog -> SetLog) via the serializer.
    """
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """
        Filters the queryset to only return workouts belonging to the current authenticated user.
        """
        # Note: We order by start_time descending by default for history views
        return Workout.objects.filter(user=self.request.user).order_by('-start_time')

    def perform_create(self, serializer):
        """
        Saves the new Workout instance, associating it with the current user.
        The nested creation logic is handled within the WorkoutSerializer.
        """
        # The user is automatically set in the serializer's create method using self.context['request'].user
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def metrics(self, request):
        """
        Custom action to retrieve simple, aggregated workout metrics for the dashboard.
        Example: Total workouts and total volume.
        """
        # Calculate total workouts
        total_workouts = self.get_queryset().count()
        
        # Calculate total volume (sum of weight * repetitions for all sets in user's workouts)
        total_volume = self.get_queryset().aggregate(
            total_volume=Sum(F('exercises__sets__weight_kg') * F('exercises__sets__repetitions'), output_field=models.DecimalField())
        )['total_volume'] or 0

        # Note: More complex metric filtering (e.g., last 7 days) should be added here
        
        return Response({
            'total_workouts': total_workouts,
            'total_volume_kg': round(total_volume, 2)
        })

class BiometricDataViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing BiometricData instances.
    """
    serializer_class = BiometricDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filters the queryset to only return biometric data belonging to the current authenticated user.
        """
        # Order by timestamp descending (most recent first)
        return BiometricData.objects.filter(user=self.request.user).order_by('-timestamp')

    def perform_create(self, serializer):
        """
        Saves the new BiometricData instance, associating it with the current user.
        """
        serializer.save(user=self.request.user)
