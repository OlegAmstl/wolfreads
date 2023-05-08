from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .forms import CreateUserForm

from books.models import Challenge, RatingBook

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
    read_books = RatingBook.objects.filter(user=user)
    read_books_of_year = read_books.filter(date_read__year='2023').count()
    if Challenge.objects.filter(user=user).exists():
        challenge = Challenge.objects.get(user=user)
        challenge_in_percent = int(int(read_books_of_year) * 100) / int(challenge.num_books)
    else:
        challenge = False
        challenge_in_percent = None
    context = {
        'user': user,
        'read_books': read_books,
        'read_books_of_year': read_books_of_year,
        'challenge': challenge,
        'challenge_percent': challenge_in_percent
    }
    return render(request, template, context=context)
