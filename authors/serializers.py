from rest_framework import serializers

from authors.models import Author


class AuthorsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="authors-detail",
    )
    
    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'url'
        )
