from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InvestorConfig(AppConfig):
    name = "apps.staff"
    verbose_name = _("staff")

    # def ready(self):
    #     try:
    #         import apps.subscription.signals  # noqa: F401
    #     except ImportError:
    #         pass
