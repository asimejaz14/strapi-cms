from django.apps import AppConfig


class UserAppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_apps'

    def ready(self):
        import user_apps.signals
