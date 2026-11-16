from django.apps import AppConfig


class UsersConfig(AppConfig):
    # UUID primary keys are declared on each model; this is the fallback for any others
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
    verbose_name = 'User Profiles and Authentication'
