from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppPurchasesConfig(AppConfig):
    name = 'app_purchases'
    verbose_name = _('purchases')
