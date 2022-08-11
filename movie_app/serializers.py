from movie_app.models import Movie, Director, Review
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'movie text stars'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movie_count'.split()


class DirectorDetailSer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title description director duration reviews rating'.split()

    def get_reviews(self, movie):
        reviews = Review.objects.filter(movie=movie)
        reviews = movie.reviews.all()
        return ReviewSerializer(reviews, many=True).data


class MovieValSer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    dir = serializers.IntegerField(min_value=1)
    dur = serializers.DurationField()
    des = serializers.CharField(required=False)

    def validate_dir(self, dir):
        try:
            Director.objects.get(id=dir)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exist!')
        return dir

    def validate_title(self, title):
        Movies = Movie.objects.filter(title=title)
        if Movies.count() > 0:
            raise ValidationError('Movie already exists!')
        return title


class MovieTitleSer(MovieValSer):
    def validate_title(self, title):
        pass


class DirectorValSer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

    def validate_name(self, name):
        Dir = Director.objects.filter(name=name)
        if Dir.count() > 0:
            raise ValidationError('Director already exists!')
        return name


class DirectorNameVal(serializers.Serializer):

    def validate_name(self, name):
        pass


class ReviewVal(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(max_value=5)

    def validate_movie(self, mov):
        try:
            Movie.objects.filter(id=mov)
        except Movie.DoesNotExist:
            raise ValidationError("Movie does not exist!")
        return mov

