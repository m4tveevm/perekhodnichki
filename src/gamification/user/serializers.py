from user.models import UserProfile

from rest_framework import serializers


__all__ = ("UserProfileSerializer",)


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = UserProfile
        fields = ["id", "username", "email", "current_level", "total_points"]
