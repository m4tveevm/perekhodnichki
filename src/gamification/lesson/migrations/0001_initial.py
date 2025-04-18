# Generated by Django 5.2 on 2025-04-13 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lesson",
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
                    "title",
                    models.CharField(
                        help_text="Название урока", max_length=255
                    ),
                ),
                (
                    "description",
                    models.TextField(help_text="Полное описание урока"),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        help_text="Порядковый номер этапа. Уроки будут отображаться согласно этому порядку."
                    ),
                ),
                (
                    "content_url",
                    models.URLField(
                        blank=True,
                        help_text="Ссылка на дополнительный контент (видео, аудио, документы и т.п.)",
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="LessonProgress",
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
                    "completed_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Дата и время завершения урока.",
                    ),
                ),
                (
                    "points_awarded",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Количество очков, начисленных за прохождение данного урока.",
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        help_text="Урок, который был пройден.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="progress_entries",
                        to="lesson.lesson",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        help_text="Профиль пользователя, выполнившего данный урок.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lesson_progress",
                        to="user.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Прогресс урока",
                "verbose_name_plural": "Прогресс уроков",
                "ordering": ["completed_at"],
                "unique_together": {("profile", "lesson")},
            },
        ),
    ]
