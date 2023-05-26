from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from books.models import Challenge, RatingBook

from .forms import CreateUserForm, AvatarForm
from .models import Avatar

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
    read_books_all = RatingBook.objects.filter(user=user).count()
    read_books_of_year = read_books.filter(date_read__year='2023').count()

    if Challenge.objects.filter(user=user).exists():
        challenge = Challenge.objects.get(user=user)
        challenge_in_percent = int((int(read_books_of_year) * 100) / int(challenge.num_books))
    else:
        challenge = False
        challenge_in_percent = None

    if Avatar.objects.filter(user=user).exists():
        avatar = Avatar.objects.get(user=user)
    else:
        avatar = False

    paginator = Paginator(read_books, settings.NUM_BOOKS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': user,
        'read_books': read_books,
        'read_books_of_year': read_books_of_year,
        'read_books_all': read_books_all,
        'challenge': challenge,
        'challenge_percent': challenge_in_percent,
        'page_obj': page_obj,
        'avatar': avatar
    }
    return render(request, template, context=context)


def add_avatar(request):
    """
    Создание аватара.
    :param request:
    :return:
    """
    template = 'users/add_avatar.html'
    if Avatar.objects.filter(user=request.user).exists():
        avatar = Avatar.objects.get(user=request.user)
        avatar.avatar.delete(save=True)
        avatar.delete()
    form = AvatarForm(request.POST or None,
                      files=request.FILES or None)
    if form.is_valid():
        avatar = form.save(commit=False)
        avatar.user = request.user
        form.save()
        return redirect('users:user_profile', request.user)
    else:
        context = {
            'form': form
        }
        return render(request, template, context=context)
