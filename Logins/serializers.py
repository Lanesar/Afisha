from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=4, max_length=20)
    password = serializers.CharField(min_length=4)


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=4)
    password = serializers.CharField(min_length=4)

    def validate_username(self, username):
        if User.objects.filter(username=username).count() > 0:
            raise ValidationError('User already exists!')
        return username
