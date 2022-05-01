from django.db import models
from django.utils.translation import gettext_lazy as _


class Collection(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    csv_file = models.FileField(upload_to="collections/%Y/%m/%d")

    class Meta:
        verbose_name = _("Collection")
        verbose_name_plural = _("Collections")

    def __str__(self):
        return f"Collection: {self.created}"
