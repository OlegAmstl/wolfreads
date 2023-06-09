from django.urls import path, re_path

from .views import (BookCreate, BookListView,
                    BookSearchView, add_read, challenge_create,
                    delete_book_from_favorites, favorite_add, favorites_list,
                    index, rating_book, book_detail, book_comment)

app_name = 'books'

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^book/create/$', BookCreate.as_view(), name='book_create'),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('fav/<int:id>/', favorite_add, name='favorite_add'),
    path('fav_del/<int:id>/', delete_book_from_favorites,
         name='favorite_delete'),
    path('favorites/', favorites_list, name='favorites_all'),
    path('read_add/<int:id>/', add_read, name='add_read'),
    path('challenge/create/', challenge_create, name='challenge_create'),
    path('rating/<int:id>/', rating_book, name='rating_book'),
    path('books/search/', BookSearchView.as_view(), name='book_search'),
    path('book/<int:book_id>/comment/', book_comment, name='book_comment')
]
