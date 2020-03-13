from books.serializers import BookSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.core.paginator import Paginator
from books.models import Book
from authors.models import Author


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        name = self.request.query_params.get('name')
        publication_year = self.request.query_params.get('publication_year')
        edition = self.request.query_params.get('edition')
        author = self.request.query_params.get('author')

        if name:
            self.queryset = self.queryset.filter(
                name__icontains=name
            )

        if publication_year:
            self.queryset = self.queryset.filter(
                publication_year=int(publication_year)
            )

        if edition:
            self.queryset = self.queryset.filter(
                edition=int(name)
            )

        if author:
            author = Author
            self.queryset = self.queryset.filter(
                authors__in=[author]
            )

        return self.queryset
