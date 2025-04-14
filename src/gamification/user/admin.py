from user.models import UserProfile

from django.contrib import admin

__all__ = ""


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "current_level",
        "total_points",
    )
    search_fields = (
        "user__username",
        "user__email",
    )
    list_filter = ("current_level",)
    fieldsets = (
        (None, {"fields": ("user",)}),
        (
            "Геймификация",
            {
                "fields": ("current_level", "total_points"),
                "description": "Параметры, "
                "отслеживающие игровой прогресс пользователя",
            },
        ),
    )
