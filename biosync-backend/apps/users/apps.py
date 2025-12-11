from django.apps import AppConfig


class UsersConfig(AppConfig):
    # Use UUID primary keys for all models in this app (matching the schema)
    default_auto_field = 'django.db.models.UUIDField'
    name = 'apps.users'
    verbose_name = 'User Profiles and Authentication'
