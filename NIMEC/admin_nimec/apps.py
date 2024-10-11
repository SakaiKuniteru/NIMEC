from django.apps import AppConfig


class AdminNimecConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "admin_nimec"

    def ready(self):
        import admin_nimec.signals 
