# Generated by Django 5.2 on 2025-04-13 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Achievement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Краткое название достижения, например 'Новичок-историк'",
                        max_length=100,
                        verbose_name="Название достижения",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Подробное описание, что означает достижение и как его можно заработать",
                        verbose_name="Описание",
                    ),
                ),
                (
                    "icon_url",
                    models.URLField(
                        blank=True,
                        help_text="Ссылка на изображение достижения в облаке, например, на CDN",
                        null=True,
                        verbose_name="URL иконки",
                    ),
                ),
                (
                    "points_required",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Минимальное количество очков, которое пользователь должен набрать для разблокировки достижения",
                        verbose_name="Требуемые очки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Достижение",
                "verbose_name_plural": "Достижения",
                "ordering": ["points_required", "name"],
            },
        ),
        migrations.CreateModel(
            name="Badge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Краткое название бейджа, например 'Хранитель традиций'",
                        max_length=100,
                        verbose_name="Название бейджа",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Детальное описание значения бейджа и условий его получения",
                        verbose_name="Описание",
                    ),
                ),
                (
                    "image_url",
                    models.URLField(
                        blank=True,
                        help_text="Ссылка на изображение бейджа в облаке (например, на CDN)",
                        null=True,
                        verbose_name="URL изображения",
                    ),
                ),
                (
                    "rarity",
                    models.CharField(
                        blank=True,
                        help_text="Уровень редкости бейджа, например 'обычный', 'редкий', 'эпический'",
                        max_length=50,
                        verbose_name="Редкость",
                    ),
                ),
            ],
            options={
                "verbose_name": "Бейдж",
                "verbose_name_plural": "Бейджи",
                "ordering": ["rarity", "name"],
            },
        ),
    ]
