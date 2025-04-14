from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from achievement.models import Achievement, Badge
from achievement.serializers import (
    AchievementSerializer,
    BadgeSerializer,
)

__all__ = ""


class AchievementModelTests(TestCase):
    def setUp(self):
        self.achievement = Achievement.objects.create(
            name="Novice Historian",
            description="Test achievement description",
            icon_url="https://storage.yandexcloud.net/updspace-s3/jwm-issue.jpg",
            points_required=100,
        )

    def test_str_method(self):
        self.assertEqual(str(self.achievement), "Novice Historian")

    def test_is_unlocked_true(self):
        self.assertTrue(self.achievement.is_unlocked(150))

    def test_is_unlocked_false(self):
        self.assertFalse(self.achievement.is_unlocked(50))

    def test_info_property(self):
        expected = "Novice Historian (Требуется 100 очков): Test achievement description"
        self.assertEqual(self.achievement.info, expected)


class BadgeModelTests(TestCase):
    def setUp(self):
        self.badge = Badge.objects.create(
            name="Heritage Keeper",
            description="Test badge description",
            image_url="https://storage.yandexcloud.net/updspace-s3/jwm-issue.jpg",
            rarity="epic",
        )
        self.badge_no_rarity = Badge.objects.create(
            name="Simple Badge",
            description="Simple badge description",
            rarity="",
        )

    def test_str_method(self):
        self.assertEqual(str(self.badge), "Heritage Keeper")

    def test_display_rarity(self):
        self.assertEqual(self.badge.display_rarity, "Epic")
        self.assertEqual(self.badge_no_rarity.display_rarity, "Не указано")

    def test_info_property(self):
        expected = "Heritage Keeper (Epic): Test badge description"
        self.assertEqual(self.badge.info, expected)


class AchievementSerializerTests(TestCase):
    def setUp(self):
        self.achievement = Achievement.objects.create(
            name="Novice Historian",
            description="Test achievement description",
            icon_url="https://storage.yandexcloud.net/updspace-s3/jwm-issue.jpg",
            points_required=100,
        )

    def test_serialize_achievement(self):
        serializer = AchievementSerializer(instance=self.achievement)
        data = serializer.data
        self.assertEqual(data["name"], "Novice Historian")
        self.assertEqual(data["description"], "Test achievement description")
        self.assertEqual(
            data["icon_url"],
            "https://storage.yandexcloud.net/updspace-s3/jwm-issue.jpg",
        )
        self.assertEqual(data["points_required"], 100)


class BadgeSerializerTests(TestCase):
    def setUp(self):
        self.badge = Badge.objects.create(
            name="Heritage Keeper",
            description="Vibe badge description",
            image_url="https://storage.yandexcloud.net/updspace-s3/jwm-issue.jpg",
            rarity="epic",
        )

    def test_serialize_badge(self):
        serializer = BadgeSerializer(instance=self.badge)
        data = serializer.data
        self.assertEqual(data["name"], "Heritage Keeper")
        self.assertEqual(data["description"], "Vibe badge description")
        self.assertEqual(
            data["image_url"],
            "https://storage.yandexcloud.net/updspace-s3/jwm-issue.jpg",
        )
        self.assertEqual(data["rarity"], "epic")


class AchievementAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="apitest", password="secret"
        )
        self.client.force_authenticate(user=self.user)
        Achievement.objects.create(
            name="Novice Historian",
            description="Test achievement description",
            icon_url="https://storage.yandexcloud.net/updspace-s3/jwm-issue.jpg",
            points_required=100,
        )

    def test_get_achievements_list(self):
        url = reverse("achievement-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


class BadgeAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="apitest2", password="secret"
        )
        self.client.force_authenticate(user=self.user)
        Badge.objects.create(
            name="Heritage Keeper",
            description="Test badge description",
            image_url="https://storage.yandexcloud.net/updspace-s3/jwm-issue.jpg",
            rarity="epic",
        )

    def test_get_badges_list(self):
        url = reverse("badge-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)

# Removed duplicate test_get_badges_list method.
