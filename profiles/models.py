from django.db import models

from friends.models import Friendship


class UserProfile(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    gender = models.CharField(max_length=1, choices=GENDERS)

    friend_list = models.ManyToManyField(Friendship)
