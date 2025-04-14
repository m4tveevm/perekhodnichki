from rest_framework import generics

from achievement.models import Achievement, Badge
from achievement.serializers import AchievementSerializer, BadgeSerializer

__all__ = ("AchievementListAPIView", "BadgeListAPIView")


class AchievementListAPIView(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class BadgeListAPIView(generics.ListAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
