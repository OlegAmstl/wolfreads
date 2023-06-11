from django.contrib import admin

from .models import Book, Challenge, Comment, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Регистрация модели Book для панели администратора.
    """

    list_display = (
        'title',
        'genre',
        'description',
        'pub_date',
        'add_date'
    )
    list_filter = (
        'genre',
        'pub_date'
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Регистарция модели Genre для панели администратора.
    """

    list_display = (
        'name',
    )


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    """
    Регистрация модели Challenge для панели администратора.
    """

    list_display = [
        'num_books',
        'user'
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Регистрация модели Comment для панели администратора.
    '''

    list_display = ['author', 'body', 'created', 'active']
    list_filter = ['active', 'author', 'created', 'update']
    search_fields = ['body', 'author']
