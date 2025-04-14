from django.db import models

from achievement.models import Achievement, Badge
from user.models import UserProfile

__all__ = ("UserAchievement", "UserBadge")


class UserAchievement(models.Model):
    profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="user_achievements"
    )
    achievement = models.ForeignKey(
        Achievement, on_delete=models.CASCADE, related_name="awarded_to"
    )
    awarded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("profile", "achievement")

    def __str__(self):
        return f"{self.profile.user.username} - {self.achievement.name}"


class UserBadge(models.Model):
    profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="user_badges"
    )
    badge = models.ForeignKey(
        Badge, on_delete=models.CASCADE, related_name="awarded_to"
    )
    awarded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("profile", "badge")

    def __str__(self):
        return f"{self.profile.user.username} - {self.badge.name}"
