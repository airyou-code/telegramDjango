from django.contrib import admin
from django.contrib.admin import ModelAdmin
from main.models import Person


@admin.register(Person)
class PersonAdmin(ModelAdmin):

    fields = (
        "username",
        "first_name",
        "last_name",
        "is_bot",
        "language_code",
        "link",
        "name",
        "user",
        "tg_id",
    )

    readonly_fields = (
        "user",
        "username",
        "first_name",
        "last_name",
        "is_bot",
        "language_code",
        "link",
        "name",
        "tg_id",
    )
