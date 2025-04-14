from user.views import UserProfileDetailAPIView

from django.urls import path

urlpatterns = [
    path(
        "profile/",
        UserProfileDetailAPIView.as_view(),
        name="user-profile-detail",
    ),
]
