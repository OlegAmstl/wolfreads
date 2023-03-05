from django.urls import path, re_path

from .views import (
    index,
    AuthorCreate,
    AuthorListView,
    AuthorUpdate,
    AuthorDelete,
    AuthorDetailView,
    BookCreate,
    BookUpdate,
    BookDelete,
    BookListView,
    BookDetailView
    )

app_name = 'books'

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^author/create/$', AuthorCreate.as_view(), name='author_create'),
    re_path(r'^author/update/(?P<pk>\d+)$', AuthorUpdate.as_view(),
            name='author_update'),
    re_path(r'^author/delete/(?P<pk>\d+)$', AuthorDelete.as_view(),
            name='author_delete'),
    re_path(r'^authors/$', AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', AuthorDetailView.as_view(),
            name='author_detail'),
    re_path(r'^book/create/$', BookCreate.as_view(), name='book_create'),
    re_path(r'^book/update/(?P<pk>\d+)$', BookUpdate.as_view(),
            name='book_update'),
    re_path(r'^book/delete/(?P<pk>\d+)$', BookDelete.as_view(),
            name='book_delete'),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(),
            name='book_detail'),
]
