from django.urls import path
from achievement.views import AchievementListAPIView, BadgeListAPIView

urlpatterns = [
    path(
        "achievement/",
        AchievementListAPIView.as_view(),
        name="achievement-list",
    ),
    path("badge/", BadgeListAPIView.as_view(), name="badge-list"),
]
