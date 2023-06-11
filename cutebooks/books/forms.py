from django import forms

from .models import Book, Challenge, Comment, RatingBook


class BookForm(forms.ModelForm):
    """
    Добавлнние и редактирование книг.
    """

    class Meta:
        model = Book
        fields = '__all__'


class ChallengeForm(forms.ModelForm):
    '''
    Добавление челленджа. Указывается число планируемых к чтению за год книг.
    '''

    class Meta:
        model = Challenge
        fields = ['num_books', ]


class RatingForm(forms.ModelForm):
    '''
    Оценивается книга по пятибальной шкале.
    '''

    class Meta:
        model = RatingBook
        fields = ['score', ]


class BookSearchForm(forms.Form):
    '''
    Поиск книги по названию.
    '''

    book_title = forms.CharField()

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book_title'].widget.attrs.update(
            {'class': 'form-control'})


class CommentForm(forms.ModelForm):
    '''
    Форма написания комментария.
    '''

    class Meta:
        model = Comment
        fields = ['body', ]


