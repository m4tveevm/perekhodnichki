from rest_framework import serializers

from achievement.serializers import (
    AchievementSerializer,
    BadgeSerializer,
)
from achievementassessment.models import (
    UserAchievement,
    UserBadge,
)

__all__ = ["UserAchievementSerializer", "UserBadgeSerializer"]


class UserAchievementSerializer(serializers.ModelSerializer):
    achievement = AchievementSerializer(read_only=True)

    class Meta:
        model = UserAchievement
        fields = ["id", "achievement", "awarded_at"]


class UserBadgeSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer(read_only=True)

    class Meta:
        model = UserBadge
        fields = ["id", "badge", "awarded_at"]
