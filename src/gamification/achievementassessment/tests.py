from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone

from user.models import UserProfile
from achievement.models import Achievement, Badge
from achievementassessment.models import UserAchievement, UserBadge


class UserAchievementBadgeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="pass123"
        )
        self.profile = UserProfile.objects.create(
            user=self.user, current_level=1, total_points=0
        )
        self.achievement1 = Achievement.objects.create(
            name="Test Achievement",
            description="Test achievement description",
            icon_url="https://storage.yandexcloud.net/updspace-s3/jwm-issue.jpg",
            points_required=10,
        )
        self.badge1 = Badge.objects.create(
            name="Test Badge",
            description="Test badge description",
            image_url="https://storage.yandexcloud.net/updspace-s3/jwm-issue.jpg",
            rarity="epic",
        )

    def test_create_user_achievement(self):
        ua = UserAchievement.objects.create(
            profile=self.profile, achievement=self.achievement1
        )

        self.assertEqual(
            str(ua), f"{self.user.username} - {self.achievement1.name}"
        )

        self.assertIsNotNone(ua.awarded_at)
        self.assertLessEqual(ua.awarded_at, timezone.now())

        self.assertIn(ua, self.profile.user_achievements.all())

    def test_unique_user_achievement(self):
        UserAchievement.objects.create(
            profile=self.profile, achievement=self.achievement1
        )
        with self.assertRaises(IntegrityError):
            UserAchievement.objects.create(
                profile=self.profile, achievement=self.achievement1
            )

    def test_create_user_badge(self):
        ub = UserBadge.objects.create(profile=self.profile, badge=self.badge1)

        self.assertEqual(str(ub), f"{self.user.username} - {self.badge1.name}")

        self.assertIsNotNone(ub.awarded_at)
        self.assertLessEqual(ub.awarded_at, timezone.now())

        self.assertIn(ub, self.profile.user_badges.all())

    def test_unique_user_badge(self):
        UserBadge.objects.create(profile=self.profile, badge=self.badge1)
        with self.assertRaises(IntegrityError):
            UserBadge.objects.create(profile=self.profile, badge=self.badge1)
