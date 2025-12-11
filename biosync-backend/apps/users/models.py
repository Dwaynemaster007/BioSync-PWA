from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Define choices outside the class for clarity
FITNESS_LEVELS = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
    ('elite', 'Elite'),
]

class User(AbstractUser):
    """
    Extends Django's default AbstractUser model to include fitness-specific profile fields.
    Uses email as the unique identifier for login.
    """
    # Overriding the default primary key to use UUID
    # Although AppConfig sets default_auto_field to UUIDField, defining it here is clearer.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Core Overrides
    email = models.EmailField(unique=True, verbose_name="Email Address")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] # Keep username for compatibility

    # Custom Profile Fields
    bio = models.TextField(blank=True, verbose_name="Biography")
    profile_picture = models.ImageField(
        upload_to='profiles/', 
        null=True, 
        blank=True,
        help_text="User's profile image."
    )
    fitness_level = models.CharField(
        max_length=20, 
        choices=FITNESS_LEVELS, 
        default='beginner',
        help_text="User's self-assessed fitness level."
    )
    height_cm = models.IntegerField(
        null=True, 
        blank=True, 
        verbose_name="Height (cm)",
        help_text="User's height in centimeters."
    )
    latest_weight_kg = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        null=True, 
        blank=True,
        verbose_name="Latest Weight (kg)",
        help_text="The user's most recently recorded weight in kilograms."
    )
    date_of_birth = models.DateField(null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
