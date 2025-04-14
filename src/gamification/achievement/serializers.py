from rest_framework import serializers

from achievement.models import Achievement, Badge

__all__ = ["AchievementSerializer", "BadgeSerializer"]


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ["id", "name", "description", "icon_url", "points_required"]


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ["id", "name", "description", "image_url", "rarity"]
