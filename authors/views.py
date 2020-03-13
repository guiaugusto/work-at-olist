from authors.serializers import AuthorsSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.core.paginator import Paginator
from authors.models import Author


class AuthorsViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorsSerializer
    queryset = Author.objects.all()

    def get_queryset(self):
        name = self.request.query_params.get('name')

        if name:
            self.queryset = self.queryset.filter(
                name__icontains=name
            )

        return self.queryset
