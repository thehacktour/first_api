from rest_framework import generics
from books.models import Book
from books.serializer import BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class BookEndPoint(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_paginated_response(self, data):
        return Response(data)