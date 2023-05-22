from django.shortcuts import render
from rest_framework import viewsets

from books.models import Book
from .serializers import BookSerializer


class IndexViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.order_by('-add_date')[:4]
    serializer_class = BookSerializer
