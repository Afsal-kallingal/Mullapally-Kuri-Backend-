from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TargetConfig(AppConfig):
    name = "apps.task"
    verbose_name = _("task")

    # def ready(self):
    #     try:
    #         import apps.subscription.signals  # noqa: F401
    #     except ImportError:
    #         pass
