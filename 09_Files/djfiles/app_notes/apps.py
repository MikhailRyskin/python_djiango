from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppNotesConfig(AppConfig):
    name = 'app_notes'
    verbose_name = _('notes')


