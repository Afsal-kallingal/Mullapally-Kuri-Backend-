from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TargetConfig(AppConfig):
    name = "apps.sales_target"
    verbose_name = _("sales_target")

    # def ready(self):
    #     try:
    #         import apps.subscription.signals  # noqa: F401
    #     except ImportError:
    #         pass
