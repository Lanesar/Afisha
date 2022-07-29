from movie_app.models import Movie, Director, Review
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'movie text'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movie_count'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title description director duration reviews rating'.split()

    def get_reviews(self, movie):
        reviews = Review.objects.filter(movie=movie)
        reviews = movie.reviews.all()
        return ReviewSerializer(reviews, many=True).data
