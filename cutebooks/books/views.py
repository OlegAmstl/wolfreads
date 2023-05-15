from datetime import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, edit

from .forms import BookSearchForm, ChallengeForm, RatingForm
from .models import Book


def index(request):
    books = Book.objects.order_by('-add_date')[:4]
    context = {
        'books': books,
    }
    return render(request, 'books/index.html', context=context)


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
    paginate_by = settings.NUM_BOOKS


class BookDetailView(DetailView):
    '''
    Отображает информацию по выбранной книге.
    '''

    model = Book


@login_required
def favorite_add(request, id):
    """
    Отображение книг, добавленных в избранное.
    :param request:
    :param id: id книги.
    :return:
    """
    book = get_object_or_404(Book, id=id)
    if book.favorites.filter(id=request.user.id).exists():
        book.favorites.remove(request.user)
    else:
        book.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def favorites_list(request):
    fav_books = Book.objects.filter(favorites=request.user)
    return render(request, 'books/favorites.html', {'fav_books': fav_books})


@login_required
def add_read(request, id):
    """
    Отображение прочитанных книг.
    :param request:
    :param id: id книги.
    :return:
    """
    book = get_object_or_404(Book, id=id)
    if book.read_user.filter(id=request.user.id).exists():
        book.read_user.remove(request.user)
    else:
        book.read_user.add(request.user)
        book.date_read = datetime.now()
        book.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def delete_book_from_favorites(request, id):
    """
    Удаление книги из списка Хочу прочитать.
    :param request:
    :return:
    """
    book = get_object_or_404(Book, id=id)
    if book.favorites.filter(id=request.user.id).exists():
        book.favorites.remove(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def challenge_create(request):
    """
    Создание челенджа.
    :param request:
    :return:
    """
    template = 'books/challenge_form.html'
    form = ChallengeForm(request.POST or None,
                         files=request.FILES or None)
    if form.is_valid():
        challenge = form.save(commit=False)
        challenge.user = request.user
        form.save()
        return redirect('users:user_profile', request.user)
    else:
        context = {
            'form': form
        }
        return render(request, template, context=context)


def rating_book(request, id):
    '''
    Оценка книги по пятибальной шкале.
    :param request:
    :param id:
    :return:
    '''
    book = get_object_or_404(Book, id=id)
    form = RatingForm(request.POST or None,
                      files=request.FILES or None)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.user = request.user
        rating.book = book
        form.save()
        return redirect('users:user_profile', request.user)
    else:
        context = {
            'form': form
        }
    return render(request, 'books/rating_book_form.html', context=context)


class BookSearchView(ListView):
    '''
    Отображение результатов поиска книги по названию.
    '''

    model = Book
    context_object_name = 'books'
    form_class = BookSearchForm
    paginate_by = settings.NUM_BOOKS

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            books = Book.objects.filter(title__icontains=form.cleaned_data['book_title'])
            return books
        return []

    def get_template_names(self):
        return 'books/search.html'
