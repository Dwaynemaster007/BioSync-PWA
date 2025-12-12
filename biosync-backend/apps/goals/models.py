from django.db import models
from apps.users.models import CustomUser

class Goal(models.Model):
    # Status Choices, matching the frontend logic (uppercase for Django constants)
    STATUS_CHOICES = [
        ('NOT_STARTED', 'Not Started'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('STUCK', 'Stuck'),
    ]

    # Type Choices (example list)
    TYPE_CHOICES = [
        ('Fitness', 'Fitness'),
        ('Learning', 'Learning'),
        ('Health', 'Health'),
        ('Work', 'Work'),
        ('Finance', 'Finance'),
        ('Other', 'Other'),
    ]

    # Basic Identification
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    # Tracking Fields
    start_date = models.DateField()
    target_date = models.DateField(blank=True, null=True)
    
    # Target Metrics
    # Max digits 12, decimal places 2 for flexibility (e.g., currency, precise measurements)
    target_value = models.DecimalField(max_digits=12, decimal_places=2, default=1.00)
    target_unit = models.CharField(max_length=50) # e.g., 'km', 'books', 'USD', 'hours'
    
    # New: Current Progress Value (This is what the frontend updates)
    current_value = models.DecimalField(max_digits=12, decimal_places=2, default=0.00) 

    # Status and Type
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOT_STARTED')
    goal_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Other')

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Ensures a user cannot have two goals with the exact same title
        unique_together = ('user', 'title',)
        ordering = ['target_date', 'status', 'title']
        verbose_name = "Goal"
        verbose_name_plural = "Goals"

    def __str__(self):
        return f"{self.user.username}'s Goal: {self.title}"

    # Custom property for progress percentage (read-only in API)
    @property
    def progress_percentage(self):
        if self.target_value <= 0:
            return 0
        return min(100, (self.current_value / self.target_value) * 100)
