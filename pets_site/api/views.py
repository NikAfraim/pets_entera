"""
Содержит View-класс для моделей:

- Type;
- Pet;
- User;
- ...
"""
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet as DjoserUserViewSet
from pet.models import Pet, Type
from rest_framework import mixins, permissions, viewsets
from user.models import User

from .filters import PetFilter
from .permissions import IsOwnerOrReadOnly
from .serializers import (PetCreateSerializer, PetReadSerializer,
                          TypeSerializer, UserReadSerializer)


class UserViewSet(DjoserUserViewSet):
    """View-класс реализующий операции модели User."""

    queryset = User.objects.all()
    serializer_class = UserReadSerializer
    permission_classes = [permissions.IsAuthenticated]


class TypeViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """View-класс реализующий операции модели Type."""

    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class PetViewSet(viewsets.ModelViewSet):
    """View-класс реализующий операции модели Pet."""

    queryset = Pet.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PetFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PetReadSerializer
        return PetCreateSerializer
