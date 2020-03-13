from rest_framework import serializers

from authors.models import Author


class AuthorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'url'
        )
