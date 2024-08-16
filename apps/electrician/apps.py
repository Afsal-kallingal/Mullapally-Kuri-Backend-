from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ElectricianConfig(AppConfig):
    name = "apps.electrician"
    verbose_name = _("electrician")

    # def ready(self):
    #     try:
    #         import apps.subscription.signals  # noqa: F401
    #     except ImportError:
    #         pass
