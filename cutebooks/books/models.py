from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Genre(models.Model):
    """
    Жанр книги.
    """

    name = models.CharField(
        max_length=150,
        verbose_name='Жанр книги',
        help_text='Укажите жанр книги'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Book(models.Model):
    """
    Модель книги.
    """

    title = models.CharField(
        max_length=150,
        verbose_name="Название книги",
        help_text='Укажите название книги'
    )
    author = models.CharField(
        max_length=250,
        verbose_name='Автор книги',
        help_text='Укажите автора/авторов книги'
    )
    description = models.TextField(
        verbose_name="Описание книги",
        help_text='Напишите аннотацию книги'
    )
    cover = models.ImageField(
        verbose_name="Обложка книги",
        help_text='Добавьте обложку книги',
        upload_to="books/books/",
        blank=True
    )
    genre = models.ForeignKey(
        Genre,
        verbose_name='Жанр',
        help_text='Укажите жанр книги',
        on_delete=models.SET_NULL,
        null=True
    )
    pub_date = models.CharField(
        max_length=50,
        verbose_name="Дата публикации",
        help_text='Укажите дату публикации'
    )
    add_date = models.DateTimeField(
        verbose_name="Дата добавления книги на сайт",
        auto_now=True
    )
    favorites = models.ManyToManyField(
        User,
        related_name='favorite',
        default=None,
        blank=True
    )
    read = models.ManyToManyField(
        User,
        related_name='read',
        default=None,
        blank=True
    )
    date_read = models.DateField(blank=True,
                                 null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Challenge(models.Model):
    """
    Модель создания челенджа на
    прочтение определенного количества книг.
    """

    num_books = models.IntegerField(verbose_name='Количество книг на год')
    year = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.num_books}'
