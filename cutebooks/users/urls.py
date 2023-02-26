from django.contrib.auth.views import LogoutView, LoginView,\
    PasswordResetView, PasswordResetDoneView,\
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from .views import SignUp, favorite_add, favorites_list, profile, add_read

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(
        template_name='users/logged_out.html'), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),

    path('password_reset/', PasswordResetView.as_view(
        template_name='users/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('fav/<int:id>/', favorite_add, name='favorite_add'),
    path('favorites/', favorites_list, name='favorites_all'),
    path('read_add/<int:id>/', add_read, name='add_read'),
    path('profile/<str:username>/', profile,
         name='user_profile')
]
