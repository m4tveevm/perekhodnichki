from django.db import models

__all__ = ("Achievement", "Badge")


class Achievement(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название достижения",
        help_text="Краткое название достижения, например 'Новичок-историк'",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
        help_text="Подробное описание, что означает достижение и как его можно заработать",
    )
    icon_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="URL иконки",
        help_text="Ссылка на изображение достижения в облаке, например, на CDN",
    )
    points_required = models.PositiveIntegerField(
        default=0,
        verbose_name="Требуемые очки",
        help_text="Минимальное количество очков, которое пользователь должен набрать для разблокировки достижения",
    )

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
        ordering = ["points_required", "name"]

    def __str__(self):
        return self.name

    def is_unlocked(self, total_points):
        return total_points >= self.points_required

    @property
    def info(self):
        return f"{self.name} (Требуется {self.points_required} очков): {self.description}"


class Badge(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название бейджа",
        help_text="Краткое название бейджа, например 'Хранитель традиций'",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
        help_text="Детальное описание значения бейджа и условий его получения",
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="URL изображения",
        help_text="Ссылка на изображение бейджа в облаке (например, на CDN)",
    )
    rarity = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Редкость",
        help_text="Уровень редкости бейджа, например 'обычный', 'редкий', 'эпический'",
    )

    class Meta:
        verbose_name = "Бейдж"
        verbose_name_plural = "Бейджи"
        ordering = ["rarity", "name"]

    def __str__(self):
        return self.name

    @property
    def display_rarity(self):
        return self.rarity.capitalize() if self.rarity else "Не указано"

    @property
    def info(self):
        return f"{self.name} ({self.display_rarity}): {self.description}"
