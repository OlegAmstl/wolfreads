from django.urls import path, re_path

from .views import (
    index,
    BookCreate,
    BookUpdate,
    BookDelete,
    BookListView,
    BookDetailView,
    favorite_add,
    favorites_list,
    add_read,
    delete_book_from_favorites,
    challenge_create,
    )

app_name = 'books'

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^book/create/$', BookCreate.as_view(), name='book_create'),
    re_path(r'^book/update/(?P<pk>\d+)$', BookUpdate.as_view(),
            name='book_update'),
    re_path(r'^book/delete/(?P<pk>\d+)$', BookDelete.as_view(),
            name='book_delete'),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(),
            name='book_detail'),
    path('fav/<int:id>/', favorite_add, name='favorite_add'),
    path('fav_del/<int:id>/', delete_book_from_favorites, name='favorite_delete'),
    path('favorites/', favorites_list, name='favorites_all'),
    path('read_add/<int:id>/', add_read, name='add_read'),
    path('challenge/create/', challenge_create, name='challenge_create'),
]
