from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    content = models.CharField(max_length=512, null=False)


class LikesRelationship(models.Model):
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now=True)


class StatusRelationship(models.Model):
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now=True)
