from django.db import models


class Friendship(models.Model):
    friend = models.ForeignKey('profiles.UserProfile')

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
