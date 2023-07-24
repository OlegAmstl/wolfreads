from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from books.models import Challenge, RatingBook

from .forms import AvatarForm, CreateUserForm
from .models import Avatar, Contact
from actions.utils import create_action

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
    """
    template = 'users/profile.html'
    # user = request.user
    user = get_object_or_404(User, username=username)
    read_books = RatingBook.objects.filter(user=user).order_by('-date_read')
    read_books_all = RatingBook.objects.filter(user=user).count()
    read_books_of_year = read_books.filter(date_read__year='2023').count()
    following = False

    if request.user.is_authenticated:
        if Contact.objects.filter(user_from=request.user, user_to=user).exists():
            following = True

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
        'avatar': avatar,
        'following': following
    }
    return render(request, template, context=context)


def add_avatar(request):
    """
    Создание аватара.
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


@login_required
def user_list(request):
    """
    Представление списка пользователей.
    """
    template = 'users/user_list.html'
    users = User.objects.all()
    context = {'users': users}
    return render(request, template, context=context)


@login_required
def user_follow(request, username):
    """
    Подписка на пользователя.
    """
    user = get_object_or_404(User, username=username)
    if user != request.user:
        Contact.objects.get_or_create(user_from=request.user,
                                      user_to=user)
        create_action(request.user, 'подписался на', user)
    return redirect('users:user_profile', username)


@login_required
def user_unfollow(request, username):
    """
    Отписка от пользователя.
    """
    user = get_object_or_404(User, username=username)
    follow = get_object_or_404(Contact, user_to=user)
    follow.delete()
    return redirect('users:user_profile', username)
