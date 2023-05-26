from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from books.models import Book, Challenge
from .serializers import BookSerializer, ChallengeSerializer


class IndexViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.order_by('-add_date')[:4]
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
