from django import forms

from .models import Book, Author


class AuthorForm(forms.ModelForm):
    """
    Добавление и редактирования автора.
    """

    class Meta:
        model = Author


class BookForm(forms.ModelForm):
    """
    Добавлнние и редактирование книг.
    """

    author = forms.ModelMultipleChoiceField(
        label='Выбрать автора',
        widget=forms.SelectMultiple,
        queryset=Author.objects.all()
    )

    class Meta:
        model = Book

