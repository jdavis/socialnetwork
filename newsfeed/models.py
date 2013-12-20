from django.contrib.auth.models import User

from django.db import models
from django.forms import ModelForm


class Status(models.Model):
    content = models.CharField(max_length=512, null=False)
    owner = models.ForeignKey('profiles.UserProfile', related_name='statuses')
    likes = models.ManyToManyField('profiles.UserProfile', related_name='liked_statuses')
    created = models.DateTimeField(auto_now=True)

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['content']


class LikesRelationship(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now=True)


class StatusRelationship(models.Model):
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now=True)
