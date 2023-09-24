from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):

    name = models.CharField(
        _("Name"),
        max_length=150,
        null=True
    )
    description = models.TextField(
        _("Description"),
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Order(models.Model):

    token = models.CharField(
        _("token"), unique=True,
        max_length=10,
        blank=True, null=True
    )
    products = models.ManyToManyField(
        Product,
        verbose_name=_("Products"),
        blank=True
    )
