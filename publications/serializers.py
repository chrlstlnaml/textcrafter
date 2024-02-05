from rest_framework import serializers
from .models import Publication, PublicationView, Vote


class PublicationSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    public_date = serializers.DateTimeField(format='%d.%m.%Y %H:%M', read_only=True)

    class Meta:
        model = Publication
        fields = ['id', 'author', 'text', 'public_date']


class PublicationViewSerializer(serializers.ModelSerializer):
    public_date = serializers.DateTimeField(format='%d.%m.%Y %H:%M', read_only=True)

    class Meta:
        model = PublicationView
        fields = ['id', 'author', 'text', 'public_date', 'rating', 'vote_count']


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    VOTE_CHOICES = ['like', 'dislike', 'revoke']
    value = serializers.ChoiceField(choices=VOTE_CHOICES)

    class Meta:
        model = Vote
        fields = ['user', 'publication', 'value']
