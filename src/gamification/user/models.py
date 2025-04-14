from django.contrib.auth.models import User
from django.db import models

__all__ = ("UserProfile",)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="Пользователь",
        help_text="Пользователь, для которого создается профиль",
    )
    current_level = models.PositiveIntegerField(
        default=1,
        verbose_name="Текущий уровень",
        help_text="Текущий уровень пользователя в системе геймификации",
    )
    total_points = models.PositiveIntegerField(
        default=0,
        verbose_name="Набранные очки",
        help_text="Общее количество очков, накопленных "
        "пользователем за выполнение квестов",
    )

    def __str__(self):
        return f"Profile: {self.user.username}"

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"
        ordering = ["user__username"]
