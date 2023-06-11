from django.shortcuts import render
from rest_framework import mixins, viewsets

from books.models import Book, Challenge

from .serializers import BookSerializer, ChallengeSerializer


class IndexViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.order_by('-add_date')[:4]
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChallengeViewSet(viewsets.ModelViewSet):
    serializer_class = ChallengeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Challenge.objects.filter(user=user)


