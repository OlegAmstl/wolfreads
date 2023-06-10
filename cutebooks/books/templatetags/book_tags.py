from django import template

from ..models import Book

register = template.Library()


@register.inclusion_tag('books/latest_books.html')
def show_latest_books(count=4):
    '''
    Последние добавленные книги.
    '''
    latest_books = Book.objects.order_by('-add_date')[:count]
    return {'latest_books': latest_books}
