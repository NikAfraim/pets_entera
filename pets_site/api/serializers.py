"""
Содержит сериализаторы для моделей:

- Type;
- Pet;
- User;
- ...
"""
from djoser.serializers import UserSerializer
from drf_extra_fields.fields import Base64ImageField
from pet.models import Pet, Type
from rest_framework import serializers
from user.models import User


class TypeSerializer(serializers.ModelSerializer):
    """Преобразование данных модели Type."""

    class Meta:
        model = Type
        fields = (
            'name',
            'slug'
        )


class ShortPetReadSerializer(serializers.ModelSerializer):
    """Преобразование данных модели Pet в короткой форме."""

    type = TypeSerializer(read_only=True)
    image = Base64ImageField(read_only=True)

    class Meta:
        model = Pet
        fields = (
            'id',
            'name',
            'type',
            'image'
        )


class UserReadSerializer(UserSerializer):
    """Преобразование данных модели User на чтение."""

    email = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()
    pet = ShortPetReadSerializer(many=True, read_only=True, source='pets')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'pet'
        )


class ShortUserReadSerializer(UserSerializer):
    """Преобразование данных модели User в короткой форме."""

    email = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )


class PetReadSerializer(serializers.ModelSerializer):
    """Преобразование данных модели Pet на чтение."""

    type = TypeSerializer(read_only=True)
    owner = ShortUserReadSerializer(read_only=True)
    image = Base64ImageField(read_only=True)

    class Meta:
        model = Pet
        fields = (
            'id',
            'name',
            'type',
            'owner',
            'image'
        )


class PetCreateSerializer(serializers.ModelSerializer):
    """Преобразование данных модели Pet на создание."""

    type = serializers.SlugRelatedField(
        queryset=Type.objects.all(),
        slug_field='slug',
    )
    owner = ShortUserReadSerializer(read_only=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = Pet
        fields = (
            'id',
            'name',
            'type',
            'owner',
            'image'
        )

    def create(self, validated_data):
        recipes = Pet.objects.create(**validated_data,
                                     owner=self.context['request'].user)
        return recipes
