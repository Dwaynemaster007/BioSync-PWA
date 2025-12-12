from django.db import models
from django.conf import settings # Import settings for the User model

class Goal(models.Model):
    """
    Represents a user-defined fitness goal, tracking objectives like weight loss, 
    strength gain, or completing a running distance.
    """

    # Constants for Goal Type
    GOAL_TYPE_CHOICES = [
        ('WEIGHT_LOSS', 'Weight Loss'),
        ('MUSCLE_GAIN', 'Muscle Gain / Strength'),
        ('CARDIO_FITNESS', 'Cardio Endurance'),
        ('BODY_COMPOSITION', 'Body Composition'),
        ('HEALTH_METRIC', 'General Health Metric'),
        ('OTHER', 'Other'),
    ]

    # Constants for Goal Status
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed / Abandoned'),
        ('PENDING', 'Pending Start'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='goals',
        help_text="The user who owns this goal."
    )
    
    goal_type = models.CharField(
        max_length=50,
        choices=GOAL_TYPE_CHOICES,
        default='OTHER',
        help_text="The primary category of the fitness objective (e.g., Weight Loss, Strength)."
    )
    
    title = models.CharField(
        max_length=150,
        help_text="A short, descriptive title for the goal (e.g., 'Bench 225 lbs', 'Run 10k')."
    )

    description = models.TextField(
        blank=True,
        help_text="Detailed description of the plan or motivation for the goal."
    )

    # Target values (e.g., lose 5 kg, run 10 km)
    target_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="The target numerical value for the goal (e.g., 5.0 for weight, 10 for distance)."
    )
    
    target_unit = models.CharField(
        max_length=20,
        blank=True,
        help_text="The unit associated with the target value (e.g., 'KG', 'KM', 'REPS', 'LBS')."
    )

    # Optional: For strength goals, relate to a WGER exercise ID
    wger_exercise_id = models.IntegerField(
        null=True,
        blank=True,
        help_text="Optional WGER exercise ID if the goal is exercise-specific (e.g., strength gain for a specific lift)."
    )

    start_date = models.DateField(
        help_text="The date the goal officially started."
    )

    target_date = models.DateField(
        null=True,
        blank=True,
        help_text="The planned deadline for achieving the goal."
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ACTIVE',
        help_text="The current status of the goal (Active, Completed, Failed)."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Fitness Goal"
        verbose_name_plural = "Fitness Goals"
        ordering = ['-start_date']

    def __str__(self):
        return f"[{self.status}] {self.user.email}'s Goal: {self.title}"
