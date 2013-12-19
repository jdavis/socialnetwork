from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

def create_profile(sender, **kwargs):
    UserProfile.objects.get_or_create(user=kwargs['instance'])

class UserProfile(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User)
    birthday = models.DateField(null=True, blank=True)

    profile_picture = models.ImageField(upload_to='photos/profiles/', 
                                        null=True, blank=True)

    gender = models.CharField(max_length=1, choices=GENDERS,
                              null=True, blank=True)

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

post_save.connect(create_profile, sender=User)
