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


class Contact(models.Model):
    """
    Промежуточная модель для подписки на пользователя.
    """

    user_from = models.ForeignKey(User,
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey(User,
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_from} подписался на {self.user_to}'


User.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Contact,
                                         related_name='followers',
                                         symmetrical=False))
