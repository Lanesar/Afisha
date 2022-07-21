from django.shortcuts import render
from movie_app.models import Movie, Director, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data)
