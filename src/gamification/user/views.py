from user.serializers import UserProfileSerializer

from rest_framework import generics, permissions

__all__ = ("UserProfileDetailAPIView",)


class UserProfileDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
