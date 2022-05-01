from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EtlConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "star_wars_explorer.etl"
    verbose_name = _("ETL")
