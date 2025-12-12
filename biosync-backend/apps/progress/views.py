from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Course, Lesson, ProgressRecord
from .serializers import CourseSerializer, LessonSerializer, ProgressRecordSerializer

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A read-only ViewSet for listing and retrieving courses.
    Courses are public information.
    """
    queryset = Course.objects.filter(is_active=True).prefetch_related('lessons')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A read-only ViewSet for listing and retrieving lessons.
    Lessons belong to a course and are generally public.
    """
    queryset = Lesson.objects.filter(is_active=True).select_related('course')
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProgressRecordViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user-specific progress records.

    - The user must be authenticated.
    - Listings are filtered to only show the current user's records.
    - On creation/update, the 'user' field is automatically set to the requesting user.
    """
    serializer_class = ProgressRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # Exclude creation, update, and deletion of all records (only use the /track action)
    http_method_names = ['get', 'head', 'options', 'post']

    def get_queryset(self):
        """
        Filters the queryset to only include progress records belonging to the current user.
        """
        return ProgressRecord.objects.filter(user=self.request.user).select_related('lesson')

    def perform_create(self, serializer):
        """
        Enforces the user to be the authenticated user when creating a new record.
        This is overridden by the @action below, but kept for safety.
        """
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['post'], url_path='track')
    def track_progress(self, request):
        """
        Custom action to track or update progress for a specific lesson.

        Expected body fields:
        {
            "lesson": <lesson_id: int>,
            "status": <status: str> (e.g., 'IN_PROGRESS', 'COMPLETED')
        }
        """
        lesson_id = request.data.get('lesson')
        status_value = request.data.get('status')
        user = request.user

        if not lesson_id or not status_value:
            return Response(
                {"detail": "Both 'lesson' ID and 'status' are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            lesson = Lesson.objects.get(pk=lesson_id)
        except Lesson.DoesNotExist:
            return Response(
                {"detail": "Lesson not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # 1. Check if a record already exists for this user and lesson
        try:
            progress_record = ProgressRecord.objects.get(user=user, lesson=lesson)
            is_new = False
        except ProgressRecord.DoesNotExist:
            progress_record = ProgressRecord(user=user, lesson=lesson, status='NOT_STARTED')
            is_new = True

        # 2. Update status and timestamps
        current_time = timezone.now()
        progress_record.status = status_value
        progress_record.last_viewed_at = current_time

        if status_value == ProgressRecord.COMPLETED and progress_record.completed_at is None:
            # Only set completed_at once, upon the first transition to 'COMPLETED'
            progress_record.completed_at = current_time
        
        # 3. Save the record
        progress_record.save()
        
        # 4. Serialize the result and return
        serializer = self.get_serializer(progress_record)
        return Response(serializer.data, status=status.HTTP_200_OK if not is_new else status.HTTP_201_CREATED)
