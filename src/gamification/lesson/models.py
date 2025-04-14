from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

from user.models import UserProfile

__all__ = ("Lesson", "LessonProgress")


class Lesson(models.Model):
    title = models.CharField(max_length=255, help_text="Название урока")
    description = models.TextField(help_text="Полное описание урока")
    order = models.PositiveIntegerField(
        help_text="Порядковый номер этапа. Уроки будут отображаться согласно этому порядку."
    )
    content_url = models.URLField(
        blank=True,
        null=True,
        help_text="Ссылка на дополнительный контент (видео, аудио, документы и т.п.)",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lesson {self.order}: {self.title}"

    def get_absolute_url(self):
        return reverse("lesson-detail", kwargs={"pk": self.pk})

    def clean(self):
        if self.order < 1:
            raise ValidationError(
                "Порядковый номер урока должен быть положительным числом."
            )

    class Meta:
        ordering = ["order"]
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class LessonProgressManager(models.Manager):
    def for_profile(self, profile):
        return self.filter(profile=profile).order_by("completed_at")


class LessonProgress(models.Model):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="lesson_progress",
        help_text="Профиль пользователя, выполнившего данный урок.",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="progress_entries",
        help_text="Урок, который был пройден.",
    )
    completed_at = models.DateTimeField(
        auto_now_add=True, help_text="Дата и время завершения урока."
    )
    points_awarded = models.PositiveIntegerField(
        default=0,
        help_text="Количество очков, начисленных за прохождение данного урока.",
    )

    objects = LessonProgressManager()

    def __str__(self):
        return f"{self.profile.user.username} - {self.lesson.title} ({self.completed_at.strftime('%Y-%m-%d')})"

    def clean(self):
        if (
            LessonProgress.objects.filter(
                profile=self.profile, lesson=self.lesson
            )
            .exclude(pk=self.pk)
            .exists()
        ):
            raise ValidationError(
                "Для данного пользователя урок уже отмечен как пройденный."
            )

    class Meta:
        unique_together = ("profile", "lesson")
        ordering = ["completed_at"]
        verbose_name = "Прогресс урока"
        verbose_name_plural = "Прогресс уроков"
