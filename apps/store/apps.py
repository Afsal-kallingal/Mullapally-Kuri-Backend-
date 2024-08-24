from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductConfig(AppConfig):
    name = "apps.store"
    verbose_name = _("store")

    # def ready(self):
    #     try:
    #         import apps.subscription.signals  # noqa: F401
    #     except ImportError:
    #         pass
