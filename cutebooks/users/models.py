from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Avatar(models.Model):
    """
    Аватар пользователя.
    """

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             )
    avatar = models.ImageField(verbose_name="Аватарка",
                               help_text="Выбирете изображение",
                               upload_to="avatars/",
                               blank=True
                               )
