from django.urls import path

from lesson.views import (
    LessonDetailAPIView,
    LessonListAPIView,
    LessonProgressListAPIView,
)

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lesson-list"),
    path(
        "lessons/<int:pk>/",
        LessonDetailAPIView.as_view(),
        name="lesson-detail",
    ),
    path(
        "lesson-progress/",
        LessonProgressListAPIView.as_view(),
        name="lesson-progress-list",
    ),
]
