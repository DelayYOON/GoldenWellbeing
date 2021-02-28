from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "email_verified",
                    "email_secret",
                    "login_method",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter 

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "birthdate",
        "is_active",
        "email_verified",
        "email_secret",
    )