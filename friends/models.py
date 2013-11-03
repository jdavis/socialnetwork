from django.db import models


class Friendship(models.Model):
    friend = models.ForeignKey('profiles.UserProfile')
