from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from .views import (SignUp, add_avatar, profile, user_list,
                    user_follow, user_unfollow)

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



    path('profile/<str:username>/', profile,
         name='user_profile'),
    path('avatar/', add_avatar, name='avatar'),
    path('user_list/', user_list, name='user_list'),
    path('users/<username>/follow/', user_follow, name='user_follow'),
    path('users/<username>/unfollow/', user_unfollow, name='user_unfollow')
]
