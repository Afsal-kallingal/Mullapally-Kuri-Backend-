from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QuotationConfig(AppConfig):
    name = "apps.quotation"
    verbose_name = _("quotation")

    # def ready(self):
    #     try:
    #         import apps.subscription.signals  # noqa: F401
    #     except ImportError:
    #         pass
