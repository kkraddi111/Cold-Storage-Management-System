from django.apps import AppConfig


class ColdstorageConfig(AppConfig):
    name = 'ColdStorage'
    
    def ready(self):
        import ColdStorage.signals
