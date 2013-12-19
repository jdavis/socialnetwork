from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
    user1 = models.ForeignKey(User, related_name='user1')
    user2 = models.ForeignKey(User, related_name='user2')

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
