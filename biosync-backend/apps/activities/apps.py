from django.apps import AppConfig


class ActivitiesConfig(AppConfig):
    # Use UUID primary keys for all models in this app
    default_auto_field = 'django.db.models.UUIDField'
    name = 'apps.activities'
    verbose_name = 'Activity Logging and Biometric Data'
