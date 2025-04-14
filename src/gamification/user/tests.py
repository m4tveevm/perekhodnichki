from user.models import UserProfile
from user.serializers import UserProfileSerializer

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

__all__ = ""


class UserProfileModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="secret",
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            current_level=2,
            total_points=150,
        )

    def test_str_method(self):
        expected = f"Profile: {self.user.username}"
        self.assertEqual(str(self.profile), expected)

    def test_profile_fields(self):
        self.assertEqual(self.profile.current_level, 2)
        self.assertEqual(self.profile.total_points, 150)


class UserProfileAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="apitestuser",
            password="secret",
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            current_level=3,
            total_points=200,
        )
        self.client.force_authenticate(user=self.user)

    def test_get_user_profile(self):
        url = reverse("user-profile-detail")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = UserProfileSerializer(instance=self.profile)
        self.assertEqual(response.data, serializer.data)

    def test_update_user_profile(self):
        url = reverse("user-profile-detail")
        data = {"current_level": 5, "total_points": 500}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.current_level, 5)
        self.assertEqual(self.profile.total_points, 500)
