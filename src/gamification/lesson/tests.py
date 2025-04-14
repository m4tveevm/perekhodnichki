from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from user.models import UserProfile
from lesson.models import Lesson, LessonProgress

__all__ = ""


class LessonModelTests(TestCase):
    def setUp(self):
        self.lesson_valid = Lesson.objects.create(
            title="Введение в историю",
            description="Описание урока о истории ЛЭТИ",
            order=1,
            content_url="https://spbetu.ru/material/0",
        )
        self.lesson_invalid = Lesson(
            title="Некорректный урок",
            description="Порядковый номер меньше 1",
            order=0,
        )

    def test_str_method(self):
        expected = "Lesson 1: Введение в историю"
        self.assertEqual(str(self.lesson_valid), expected)

    def test_get_absolute_url(self):
        url = self.lesson_valid.get_absolute_url()
        self.assertIn(str(self.lesson_valid.pk), url)

    def test_clean_order_validation(self):
        with self.assertRaises(ValidationError):
            self.lesson_invalid.clean()


class LessonProgressModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            current_level=1,
            total_points=50,
        )
        self.lesson1 = Lesson.objects.create(
            title="Урок 1",
            description="Описание урока 1",
            order=1,
        )
        self.lesson2 = Lesson.objects.create(
            title="Урок 2",
            description="Описание урока 2",
            order=2,
        )
        self.progress1 = LessonProgress.objects.create(
            profile=self.profile,
            lesson=self.lesson1,
            points_awarded=20,
        )

    def test_str_method(self):
        expected = (
            f"{self.profile.user.username} - "
            f"{self.lesson1.title} "
            f"({self.progress1.completed_at.strftime('%Y-%m-%d')})"
        )
        self.assertEqual(str(self.progress1), expected)

    def test_unique_progress_clean(self):
        duplicate_progress = LessonProgress(
            profile=self.profile,
            lesson=self.lesson1,
            points_awarded=10,
        )
        with self.assertRaises(ValidationError):
            duplicate_progress.clean()

    def test_manager_for_profile(self):
        progress2 = LessonProgress.objects.create(  # noqa F841
            profile=self.profile,
            lesson=self.lesson2,
            points_awarded=30,
        )
        qs = LessonProgress.objects.for_profile(self.profile)
        self.assertEqual(qs.count(), 2)
        dates = list(qs.values_list("completed_at", flat=True))
        self.assertEqual(dates, sorted(dates))


class LessonAPITests(APITestCase):
    def setUp(self):
        Lesson.objects.create(
            title="Урок API 1",
            description="Описание урока API 1",
            order=1,
            content_url="https://spbetu.ru/material/api1",
        )
        Lesson.objects.create(
            title="Урок API 2",
            description="Описание урока API 2",
            order=2,
        )

    def test_get_lessons_list(self):
        url = reverse("lesson-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)


class LessonProgressAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="apitestuser",
            password="testpass",
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            current_level=1,
            total_points=100,
        )
        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(
            title="Урок API Progress",
            description="Описание урока для прогресса",
            order=1,
        )
        LessonProgress.objects.create(
            profile=self.profile,
            lesson=self.lesson,
            points_awarded=50,
        )

    def test_get_lesson_progress_list(self):
        url = reverse("lesson-progress-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
