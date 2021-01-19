from django.db import models
from django.contrib.auth.models import User


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text