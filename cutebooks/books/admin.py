from django.contrib import admin

from .models import Book, Author, Genre


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


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Регистрация модели Author для панели администратора.
    """

    list_display = (
        'first_name',
        'last_name',
        'photo'
    )
    list_filter = (
        'last_name',
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Регистарция модели Genre для панели администратора.
    """

    list_display = (
        'name',
    )
