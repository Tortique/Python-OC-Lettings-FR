from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Model to represent a user's profile.

    Attributes:
        user (models.OneToOneField): A one-to-one relationship with the User model,
         linking the profile to a user.
        favorite_city (models.CharField): The user's favorite city (up to 64 characters),
         which can be blank.

    Methods:
        __str__(): Returns a string representation of the profile,
         which is the username of the associated user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
