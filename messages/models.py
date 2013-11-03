from django.db import models


class Message(models.Model):
    content = models.TextField(blank=False)

    sender = models.ForeignKey('profiles.UserProfile')
    recepient = models.ForeignKey('profiles.UserProfile')

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
