from django.apps import AppConfig


class JournalConfig(AppConfig):
    """
    Provides primary key type for blog app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'journal'
