from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, min_length=2)
    genres = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = Movie
        fields = ['id','title','genres','up_votes','down_votes', 'release_date']

class MovieVoteSerializer(serializers.ModelSerializer):
    ThumpsUp = (
        ('Up','upvote'),
        ('Down','downvote')
    )
    type = serializers.ChoiceField(choices=ThumpsUp)

    class Meta:
        model = Movie


