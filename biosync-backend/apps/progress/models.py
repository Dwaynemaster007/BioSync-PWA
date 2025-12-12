from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# --- Base Models for Content Structure ---

class Course(models.Model):
    """
    Represents a full course or learning module.
    """
    title = models.CharField(_("Course Title"), max_length=255, unique=True)
    description = models.TextField(_("Description"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
        ordering = ['title']

    def __str__(self):
        return self.title

class Lesson(models.Model):
    """
    Represents an individual lesson or unit within a Course.
    """
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name=_("Course")
    )
    title = models.CharField(_("Lesson Title"), max_length=255)
    content_url = models.URLField(
        _("Content URL"),
        max_length=500,
        help_text=_("URL pointing to the lesson content (e.g., video, document).")
    )
    order = models.PositiveIntegerField(
        _("Order"),
        default=0,
        help_text=_("The sequential order of the lesson within the course.")
    )
    is_active = models.BooleanField(_("Is Active"), default=True)

    class Meta:
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")
        # Ensures that a lesson title and order are unique within a single course
        unique_together = ('course', 'title')
        unique_together = ('course', 'order')
        ordering = ['course__title', 'order']

    def __str__(self):
        return f"{self.course.title}: {self.order}. {self.title}"


# --- Model for Tracking User Progress ---

class ProgressRecord(models.Model):
    """
    Tracks a specific user's progress through a specific Lesson.
    This is the core data model for the 'progress' application.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='progress_records',
        verbose_name=_("User")
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='progress_records',
        verbose_name=_("Lesson")
    )
    completed_at = models.DateTimeField(
        _("Completed At"),
        null=True,
        blank=True,
        help_text=_("Timestamp when the user marked the lesson as complete.")
    )
    last_viewed_at = models.DateTimeField(
        _("Last Viewed At"),
        auto_now=True,
        help_text=_("Timestamp of the last time the user accessed the lesson.")
    )
    status = models.CharField(
        _("Status"),
        max_length=20,
        choices=[
            ('NOT_STARTED', _('Not Started')),
            ('IN_PROGRESS', _('In Progress')),
            ('COMPLETED', _('Completed')),
        ],
        default='NOT_STARTED'
    )

    class Meta:
        verbose_name = _("Progress Record")
        verbose_name_plural = _("Progress Records")
        # A user can only have one progress record per lesson
        unique_together = ('user', 'lesson')
        ordering = ['user', 'lesson__order']

    def __str__(self):
        completion_status = "Completed" if self.completed_at else self.status
        return f"User {self.user.pk} progress on {self.lesson.title}: {completion_status}"
