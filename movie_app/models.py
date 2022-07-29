from django.db import models
from django.db.models import Avg, Count
# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def movie_count(self):
        return Movie.objects.filter(director=self).count()


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    duration = models.DurationField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')

    def __str__(self):
        return self.title

    @property
    def rating(self):
        return Review.objects.aggregate(Avg('stars'))


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=1)

    def __str__(self):
        return self.text
