from django.apps import AppConfig


class GoalsConfig(AppConfig):
    # Use the full dotted path to avoid naming collisions
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.goals'
    verbose_name = 'Fitness Goals'
