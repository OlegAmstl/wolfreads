from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Avatar

User = get_user_model()


class CreateUserForm(UserCreationForm):
    """
    Форма регистрации новых пользователей.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email'
        ]


class AvatarForm(forms.ModelForm):
    """
    Форма загрузки аватарки.
    """

    class Meta:
        model = Avatar
        fields = ["avatar", ]
