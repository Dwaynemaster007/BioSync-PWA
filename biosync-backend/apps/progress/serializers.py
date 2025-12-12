from rest_framework import serializers
from .models import Course, Lesson, ProgressRecord
from django.contrib.auth import get_user_model

User = get_user_model()

# --- Nested Serializers (Read-Only) ---

class SimpleLessonSerializer(serializers.ModelSerializer):
    """
    A simplified serializer for listing lessons within a course.
    """
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'order')
        read_only_fields = fields


# --- Core Serializers ---

class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Course model. Includes nested lessons for detailed view.
    """
    # Use the simplified serializer to list lessons within the course detail view
    lessons = SimpleLessonSerializer(many=True, read_only=True)
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'created_at', 'updated_at', 'lessons', 'lesson_count')
        read_only_fields = ('created_at', 'updated_at', 'lessons', 'lesson_count')

    def get_lesson_count(self, obj):
        """Calculates the total number of lessons in the course."""
        return obj.lessons.count()


class LessonSerializer(serializers.ModelSerializer):
    """
    Serializer for the Lesson model.
    """
    course_title = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'course', 'course_title', 'title', 'content_url', 'order', 'is_active')
        read_only_fields = ('course_title',) # course field is needed for creation/update


class ProgressRecordSerializer(serializers.ModelSerializer):
    """
    Serializer for tracking user progress on a lesson.
    The user is automatically set upon creation/update.
    """
    lesson_title = serializers.CharField(source='lesson.title', read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True) # Exposes the user ID

    class Meta:
        model = ProgressRecord
        fields = ('id', 'user_id', 'lesson', 'lesson_title', 'status', 'completed_at', 'last_viewed_at')
        read_only_fields = ('last_viewed_at', 'completed_at') # Timestamps are managed by the model/view logic

    def validate(self, data):
        """
        Custom validation to ensure 'completed_at' is set only if status is 'COMPLETED'.
        """
        status = data.get('status')

        if status == 'COMPLETED' and 'completed_at' in self.fields and data.get('completed_at') is None:
             # In view logic, we will set completed_at when the user submits 'COMPLETED'
             pass # Allow view logic to handle the timestamp
        elif status != 'COMPLETED' and data.get('completed_at') is not None:
             raise serializers.ValidationError({"completed_at": "Completed time cannot be set if status is not 'COMPLETED'."})

        return data
