from django.apps import AppConfig


class ActivitiesConfig(AppConfig):
    # UUID primary keys are declared on each model; this is the fallback for any others
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.activities'
    verbose_name = 'Activity Logging and Biometric Data'
