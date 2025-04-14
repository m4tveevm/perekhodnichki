from rest_framework import serializers
from .models import Lesson, LessonProgress


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "title",
            "description",
            "order",
            "content_url",
            "created_at",
        ]


class LessonProgressSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = LessonProgress
        fields = ["id", "profile", "lesson", "completed_at", "points_awarded"]
