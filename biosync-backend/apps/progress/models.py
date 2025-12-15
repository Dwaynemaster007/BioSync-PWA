from django.db import models
from apps.goals.models import Goal # Import the Goal model
from django.conf import settings

class ProgressEntry(models.Model):
    """
    Represents a specific, dated entry of progress towards a Goal.
    For example, logging '5 km' run today against a 'Run 100 km' goal.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        help_text="The user who made this entry."
    )
    goal = models.ForeignKey(
        Goal, 
        on_delete=models.CASCADE, 
        related_name='progress_entries',
        help_text="The goal this entry contributes to."
    )
    date = models.DateField(
        help_text="The date the progress was achieved."
    )
    value = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="The numerical value of the progress made (e.g., 5.00)."
    )
    notes = models.TextField(
        blank=True, 
        null=True, 
        help_text="Optional notes about this progress entry."
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Progress Entries"
        ordering = ['-date', '-created_at']
        # Ensure a user cannot log multiple progress entries for the same goal on the same day
        unique_together = ('goal', 'date') 

    def __str__(self):
        return f"{self.user.username}'s progress on {self.goal.title} ({self.date}): {self.value}"
    
    # NOTE: The actual cumulative value update logic (Goal.current_value) is handled in the Serializer's create method.
