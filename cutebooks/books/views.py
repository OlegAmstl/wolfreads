from datetime import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, edit

from .forms import BookSearchForm, ChallengeForm, CommentForm, RatingForm
from .models import Book
from actions.utils import create_action
from actions.models import Action


def index(request):
    """
    На главной странице отображаются последние добавленные на сайт 4 книги.
    """
    return render(request, 'books/index.html')


@login_required
def action_list(request):
    following_ids = request.user.following.values_list('id',
                                                       flat=True)
    if favorite_add:
        actions = Action.objects.filter(user_id__in=following_ids)
        return render(request, 'actions/action_list.html', {'actions': actions})
    actions = None
    return render(request, 'actions/action_list.html', {'actions': actions})


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


class BookListView(ListView):
    """
    Отображение книг.
    """

    model = Book
    paginate_by = settings.NUM_BOOKS


@require_POST
def book_comment(request, book_id):
    """
    Представление комментария в посте.
    """
    template = 'books/comment.html'
    book = get_object_or_404(Book,
                             id=book_id)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.book = book
        comment.author = request.user
        comment.save()
    context = {
        'book': book,
        'form': form,
        'comment': comment
    }
    return render(request, template, context=context)


def book_detail(request, book_id):
    template = 'books/book_detail.html'
    book = get_object_or_404(Book, id=book_id)
    comments = book.comments.filter(active=True)
    form = CommentForm()
    context = {
        'book': book,
        'comments': comments,
        'form': form
    }
    return render(request, template, context=context)


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
        create_action(request.user, 'хочет прочитать', book)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def favorites_list(request):
    '''
    Представление списка книг на прочтение.
    '''
    fav_books = Book.objects.filter(favorites=request.user)
    return render(request, 'books/favorites.html', {'fav_books': fav_books})


@login_required
def add_read(request, id):
    """
    Отображение прочитанных книг.
    """
    book = get_object_or_404(Book, id=id)
    if book.read_user.filter(id=request.user.id).exists():
        book.read_user.remove(request.user)
    else:
        book.read_user.add(request.user)
        book.date_read = datetime.now()
        book.save()
        create_action(request.user, 'прочитал', book)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def delete_book_from_favorites(request, id):
    """
    Удаление книги из списка Хочу прочитать.
    """
    book = get_object_or_404(Book, id=id)
    if book.favorites.filter(id=request.user.id).exists():
        book.favorites.remove(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def challenge_create(request):
    """
    Создание челенджа.
    """
    template = 'books/challenge_form.html'
    form = ChallengeForm(request.POST or None,
                         files=request.FILES or None)
    if form.is_valid():
        challenge = form.save(commit=False)
        challenge.user = request.user
        form.save()
        create_action(request.user, 'создал челлендж', challenge)
        return redirect('users:user_profile', request.user)
    else:
        context = {
            'form': form
        }
        return render(request, template, context=context)


def rating_book(request, id):
    '''
    Оценка книги по пятибальной шкале.
    '''
    book = get_object_or_404(Book, id=id)
    form = RatingForm(request.POST or None,
                      files=request.FILES or None)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.user = request.user
        rating.book = book
        form.save()
        create_action(request.user, 'прочитал', book)
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
