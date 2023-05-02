from django import forms

from .models import Book, Author, Challenge


class AuthorForm(forms.ModelForm):
    """
    Добавление и редактирования автора.
    """

    class Meta:
        model = Author
        fields = '__all__'


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
        fields = '__all__'


class ChallengeForm(forms.ModelForm):

    class Meta:
        model = Challenge
        fields = ['num_books',]

