from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import edit, ListView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Book, Author


def index(request):
    books = Book.objects.order_by('-add_date')[:4]
    context = {
        'books': books,
    }
    return render(request, 'books/index.html', context=context)


class AuthorCreate(edit.CreateView):
    """
    Добавления нового автора в базу данных.
    """

    model = Author
    fields = '__all__'
    success_url = reverse_lazy('books:authors')


class AuthorUpdate(edit.UpdateView):
    '''
    Редактирование информации о авторе.
    '''

    model = Author
    fields = '__all__'
    success_url = reverse_lazy('books:authors')


class AuthorDelete(edit.DeleteView):
    '''
    Удаление автора.
    '''

    model = Author
    success_url = reverse_lazy('books:authors')


class AuthorListView(ListView):
    """
    Отображение авторов.
    """

    model = Author


class AuthorDetailView(DetailView):
    """
    Персональная страница автора.
    """

    model = Author


class BookCreate(edit.CreateView):
    """
    Добавление новой кнги в базу данных.
    """

    model = Book
    fields = [
        'title',
        'author',
        'description',
        'pub_date',
        'genre',
        'cover'
    ]
    success_url = reverse_lazy('books:books')


class BookUpdate(edit.UpdateView):
    '''
    Редактирование информации о книге.
    '''

    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books:books')


class BookDelete(edit.DeleteView):
    '''
    Удаление униги из базы данных.
    '''

    model = Book
    success_url = reverse_lazy('books:books')


class BookListView(ListView):
    """
    Отображение книг.
    """

    model = Book


class BookDetailView(DetailView):
    '''
    Отображает информацию по выбранной книге.
    '''

    model = Book
