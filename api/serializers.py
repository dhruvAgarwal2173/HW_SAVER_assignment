from rest_framework import serializers
from .models import Favourites
from django.contrib.auth.models import User


class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = ('text', )


class UserFavouritesSerializer(serializers.ModelSerializer):
    favourites = FavouritesSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', )
