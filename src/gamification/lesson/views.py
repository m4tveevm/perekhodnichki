from lesson.models import Lesson, LessonProgress
from lesson.serializers import LessonProgressSerializer, LessonSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny

__all__ = (
    "LessonListAPIView",
    "LessonDetailAPIView",
    "LessonProgressListAPIView",
)


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]


class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]


class LessonProgressListAPIView(generics.ListAPIView):
    queryset = LessonProgress.objects.all()
    serializer_class = LessonProgressSerializer
    permission_classes = [AllowAny]
