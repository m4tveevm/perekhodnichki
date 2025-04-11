from django.apps import AppConfig

__all__ = ["UserConfig"]


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
