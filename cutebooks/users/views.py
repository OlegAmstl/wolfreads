from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .forms import CreateUserForm

from books.models import Book, Challenge

User = get_user_model()


class SignUp(CreateView):
    """
    Отображение формы регистрации нового пользователя.
    """

    form_class = CreateUserForm
    success_url = reverse_lazy('books:index')
    template_name = 'users/signup.html'


@login_required
def profile(request, username):
    """
    Отображение персональной страницы пользователя.
    :param request:
    :param username:
    :return:
    """
    template = 'users/profile.html'
    user = request.user
    read_books = Book.objects.filter(read=request.user)
    read_books_of_year = read_books.filter(date_read__year='2023').count()
    challenge = Challenge.objects.get(user=user)
    context = {
        'user': user,
        'read_books': read_books,
        'read_books_of_year': read_books_of_year,
        'challenge': challenge
    }
    return render(request, template, context=context)
