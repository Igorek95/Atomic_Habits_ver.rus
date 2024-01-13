from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializerPrivateUpdate, UserSerializerPublic, UserSerializerPrivateDetails
from users.services import last_login_blocker


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerPrivateUpdate  # Используй тот же сериалайзер для создания и обновления
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializerPrivateUpdate
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        serializer.save(telegram_chat_id=self.request.data.get('telegram_chat_id', None))


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializerPrivateUpdate
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerPublic
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializerPrivateDetails
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.get_object() == self.request.user:
            return UserSerializerPrivateDetails
        else:
            return UserSerializerPublic

    def get_object(self):
        pk = self.kwargs.get('pk', self.request.user.pk)
        return User.objects.get(pk=pk)
