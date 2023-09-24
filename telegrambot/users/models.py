from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from core.models import CreateUpdateTracker
from django.db import models

from telegram import Update
from telegram.ext import CallbackContext


class Person(CreateUpdateTracker):
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE,
    #     null=True
    # )

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        validators=[
            UnicodeUsernameValidator()
        ],
        error_messages={
            "unique": _("A user with that username already exists."),
        }, null=True
    )
    first_name = models.CharField(
        _("first name"), max_length=150, null=True, blank=True
    )
    last_name = models.CharField(
        _("last name"), max_length=150, null=True, blank=True
    )

    tg_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True, null=True
    )
    is_bot = models.BooleanField(
        default=False, null=True
    )
    # can_join_groups: None
    # can_read_all_group_messages: None
    # is_premium: None
    language_code = models.CharField(
        max_length=20,
        blank=True, null=True
    )
    last_name: None
    link = models.CharField(
        max_length=100,
        blank=True, null=True
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_user_and_created(cls, update: Update, context: CallbackContext):
        """ python-telegram-bot's Update, Context --> User instance """
        user = update.message.from_user
        u, created = cls.objects.update_or_create(
            tg_id=user.id,
            defaults={
                "first_name": user.first_name,
                "username": user.username,
                "is_bot": user.is_bot,
                "language_code": user.language_code,
                "link": user.link,
                "name": user.name,
            }
        )

        return u, created


# class Product(models.Model):

#     name = models.CharField(
#         _("Name"),
#         max_length=150,
#         null=True
#     )
#     description = models.TextChoices(
#         _("Description"),
#         null=True, blank=True
#     )

#     def __str__(self):
#         return f"{self.name}"

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)


# class Order(models.Model):

#     token = models.CharField(
#         _("token"), unique=True,
#         max_length=10,
#         blank=True, null=True
#     )
#     products = models.ManyToManyField(
#         verbose_name=_("Products"),
#         blank=True
#     )
