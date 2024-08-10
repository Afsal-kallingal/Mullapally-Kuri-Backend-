from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClientConfig(AppConfig):
    name = "apps.client"
    verbose_name = _("client")

    # def ready(self):
    #     try:
    #         import apps.subscription.signals  # noqa: F401
    #     except ImportError:
    #         pass
