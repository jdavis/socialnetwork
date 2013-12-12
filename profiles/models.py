from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

def create_profile(sender, **kwargs):
    profile = UserProfile(user=kwargs['instance'])
    profile.save()

class UserProfile(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    birthday = models.DateField(null=True)

    profile_picture = models.ImageField(upload_to='photos/profiles/', null=True)

    gender = models.CharField(max_length=1, choices=GENDERS, null=True)

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)


class StatusUpdate(models.Model):
    content = models.TextField(blank=False)
    thumbnail = models.ImageField(upload_to='photos/thumbs/')

    creator = models.ForeignKey(UserProfile)

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

post_save.connect(create_profile, sender=User)
