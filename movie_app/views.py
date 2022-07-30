from django.shortcuts import render
from movie_app.models import Movie, Director, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, \
    MovieDetailSerializer, DirectorDetailSer
from django.utils.dateparse import parse_duration


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        director = request.data.get('dir')
        duration = parse_duration(request.data.get('dur'))
        description = request.data.get('des')
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


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        name = request.data.get('name')
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
        name = request.data.get('name')
        dire.name = name
        dire.save()
        return Response(data=DirectorDetailSer(dire).data)
    else:
        dire.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
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





