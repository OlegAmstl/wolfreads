from re import match

from django.contrib.auth import get_user_model, password_validation
from django.core import exceptions
from rest_framework import serializers

from books.models import Book, Challenge

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания пользователя с проверкой на валидность пароля и
    имени пользователя.
    """
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    password = serializers.CharField(max_length=150,
                                     write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        ]

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_password(self, value):
        """
        Проверка валидности пароля.
        :param value:
        :return:
        """
        try:
            password_validation.validate_password(value)
        except exceptions.ValidationError as err:
            raise serializers.ValidationError(list(err))
        return value

    def validate_username(self, value):
        """
        Проверка валидности имени пользователя.
        :param value:
        :return:
        """
        pattern = r'^[\w.@+-]+\Z'
        if match(pattern, value):
            return value
        raise serializers.ValidationError(
            f'Имя пользователя должно соответствовать шаблону {pattern}.'
        )


class UserChangePasswordSerializer(serializers.Serializer):
    """
    Сериализатор изменения пароля.
    """
    current_password = serializers.CharField()
    new_password = serializers.CharField(max_length=150)

    def validate_current_password(self, value):
        user = self.context.get('user')
        if user.check_password(value):
            return value
        raise serializers.ValidationError(
            'Пароль не подходит под условия.'
        )

    def validate_new_password(self, value):
        try:
            password_validation.validate_password(value)
        except exceptions.ValidationError as err:
            raise serializers.ValidationError(list(err))
        return value


class BookSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели книги.
    """

    class Meta:
        model = Book
        fields = '__all__'


class ChallengeSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели челленджа
    """

    class Meta:
        model = Challenge
        fields = '__all__'
        read_only_fields = ['user', ]
