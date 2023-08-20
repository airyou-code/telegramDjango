from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    User
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        null=True
    )

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

    def save(self, *args, **kwargs):
        if not self.id:
            self.user = User.objects.create(
                first_name=self.first_name or "",
                last_name=self.last_name or "",
                username=self.username
            )
        super().save(*args, **kwargs)
