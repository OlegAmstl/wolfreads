from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


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
