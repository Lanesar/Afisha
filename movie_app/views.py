from django.shortcuts import render
from movie_app.models import Movie, Director, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, \
    MovieDetailSerializer, DirectorDetailSer, MovieValSer, MovieTitleSer, DirectorValSer, DirectorNameVal, ReviewVal
from django.utils.dateparse import parse_duration
from rest_framework.views import APIView

# @api_view(['GET', 'POST'])
# def movies_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         data = MovieSerializer(movies, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = MovieValSer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializer.errors})
#         title = serializer.validated_data.get('title')
#         director = serializer.validated_data.get('dir')  # here
#         duration = parse_duration(request.data.get('dur'))
#         description = serializer.validated_data.get('des')
#         final = Movie.objects.create(title=title, duration=duration, description=description, director_id=director)
#         return Response(data=MovieSerializer(final).data)


class MoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)

    def post(self, request):
        serializer = MovieValSer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        title = serializer.validated_data.get('title')
        director = serializer.validated_data.get('dir')  # here
        duration = parse_duration(request.data.get('dur'))
        description = serializer.validated_data.get('des')
        final = Movie.objects.create(title=title, duration=duration, description=description, director_id=director)
        return Response(data=MovieSerializer(final).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieDetailSerializer(movie).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = MovieTitleSer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        title = request.data.get('title')
        director = request.data.get('dir')
        duration = parse_duration(request.data.get('dur'))
        description = request.data.get('des')
        movie.title = title
        movie.director_id = director
        movie.duration = duration
        movie.description = description
        movie.save()
        return Response(data=MovieDetailSerializer(movie).data)
    else:
        movie.delete()
        return Response(status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def directors_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         data = DirectorSerializer(directors, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = DirectorValSer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializer.errors})
#         name = serializer.validated_data.get('name')
#         final = Director.objects.create(name=name)
#         return Response(data=DirectorSerializer(final).data)


class DirectorsView(APIView):
    def get(self, request):
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)

    def post(self, request):
        serializer = DirectorValSer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        name = serializer.validated_data.get('name')
        final = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(final).data)


@api_view(['GET', 'PUT', 'DELETE'])
def dir_view(request, id):
    try:
        dire = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorDetailSer(dire).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = DirectorNameVal(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        name = request.data.get('name')
        dire.name = name
        dire.save()
        return Response(data=DirectorDetailSer(dire).data)
    else:
        dire.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def reviews_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         data = ReviewSerializer(reviews, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = ReviewVal(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                             data={'errors': serializer.errors})
#         text = serializer.validated_data.get('text')
#         movie = serializer.validated_data.get('movie')
#         stars = serializer.validated_data.get('stars')
#         final = Review.objects.create(text=text, movie_id=movie, stars=stars)
#         return Response(data=ReviewSerializer(final).data)


class ReviewsView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)

    def post(self, request):
        serializer = ReviewVal(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        text = serializer.validated_data.get('text')
        movie = serializer.validated_data.get('movie')
        stars = serializer.validated_data.get('stars')
        final = Review.objects.create(text=text, movie_id=movie, stars=stars)
        return Response(data=ReviewSerializer(final).data)

@api_view(['GET', 'PUT', 'DELETE'])
def rev_view(request, id):
    try:
        rev = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(rev).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ReviewVal(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        rev.text = text
        rev.movie_id = movie
        rev.stars = stars
        rev.save()
        return Response(data=ReviewSerializer(rev).data)
    else:
        rev.delete()
        return Response(status.HTTP_204_NO_CONTENT)
