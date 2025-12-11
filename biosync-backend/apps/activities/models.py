from django.db import models
from django.conf import settings
import uuid

# --- Choices ---
ACTIVITY_TYPES = [
    ('weightlifting', 'Weightlifting'),
    ('cardio', 'Cardio'),
    ('hiit', 'HiiT'),
    ('other', 'Other'),
]

# --- Core Activity Logging (3-Tier Structure) ---

class Workout(models.Model):
    """
    Represents a single, complete training session.
    This is the top level of the activity log hierarchy.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=255, blank=True, null=True, help_text="Optional title for the workout session.")
    start_time = models.DateTimeField(help_text="The time the workout started.")
    end_time = models.DateTimeField(null=True, blank=True, help_text="The time the workout ended.")
    duration_minutes = models.IntegerField(null=True, blank=True)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES, default='weightlifting')
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s {self.activity_type} on {self.start_time.strftime('%Y-%m-%d')}"


class ExerciseLog(models.Model):
    """
    Details a single exercise performed within a specific Workout session.
    It links the Workout to an external exercise database ID (WGER) or a custom name.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    
    # Metadata about the exercise itself
    wger_exercise_id = models.IntegerField(null=True, blank=True, help_text="ID from WGER exercise API.")
    custom_name = models.CharField(max_length=255, help_text="The name of the exercise (e.g., 'Barbell Squat').")
    
    # Tracking the order for display
    order_in_workout = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.custom_name} in {self.workout.title or self.workout.id}"


class SetLog(models.Model):
    """
    The granular performance data for one single set of an ExerciseLog.
    This is where weight, reps, and RPE are recorded.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exercise_log = models.ForeignKey(ExerciseLog, on_delete=models.CASCADE, related_name='sets')
    
    set_number = models.IntegerField()
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, help_text="Weight lifted in kilograms.")
    repetitions = models.IntegerField(help_text="Number of reps completed.")
    rpe = models.IntegerField(null=True, blank=True, help_text="Rate of Perceived Exertion (1-10).")
    to_failure = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['set_number']

    def __str__(self):
        return f"Set {self.set_number}: {self.repetitions} reps @ {self.weight_kg}kg"


# --- Biometric Data ---

class BiometricData(models.Model):
    """
    Tracks time-series data for vitals (HRV, Sleep, ReadinessScore).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='biometrics')
    timestamp = models.DateTimeField(help_text="The exact time the metric was recorded.")
    
    # Weight (separated from user profile for time-series tracking)
    recorded_weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Recorded weight in kg at this timestamp.")

    # Sleep/Recovery Metrics
    sleep_duration_hours = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sleep_score = models.IntegerField(null=True, blank=True, help_text="Sleep quality score (e.g., 0-100).")
    
    # Heart/Readiness Metrics
    resting_heart_rate = models.IntegerField(null=True, blank=True, help_text="RHR in bpm.")
    heart_rate_variability = models.IntegerField(null=True, blank=True, help_text="HRV in milliseconds (ms).")
    
    # Summary Score
    readiness_score = models.IntegerField(null=True, blank=True, help_text="Overall recovery score (e.g., 0-100).")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensure fast lookup by time
        ordering = ['-timestamp'] 
        verbose_name_plural = "Biometric Data"
