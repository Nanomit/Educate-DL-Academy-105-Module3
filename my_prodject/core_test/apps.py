from django.apps import AppConfig


class CoreTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_test'

def ready(self):
    from.import signals
    