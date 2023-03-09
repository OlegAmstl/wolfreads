from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from datetime import datetime

from .forms import CreateUserForm
from books.models import Book

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
    template = 'users/profile.html'
    user = request.user
    read_books = Book.objects.filter(read=request.user)
    num_read = Book.objects.filter(read=request.user).count()
    context = {
        'user': user,
        'read_books': read_books,
        'num_read': num_read
    }
    return render(request, template, context=context)
