from django import forms

from .models import Book, Challenge


class BookForm(forms.ModelForm):
    """
    Добавлнние и редактирование книг.
    """

    class Meta:
        model = Book
        fields = '__all__'


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['num_books', ]
