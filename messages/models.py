from django.db import models


class Message(models.Model):
    content = models.TextField(blank=False)

    viewed = models.BooleanField(default=False)
    sender = models.ForeignKey('profiles.UserProfile', related_name='messages_to')
    recepient = models.ForeignKey('profiles.UserProfile', related_name='messages_from')

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
