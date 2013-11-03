from django.db import models


class UserProfile(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    # TODO: Hookup when Shawn pushes auth code
    # user = models.ForeignKey(User)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()

    profile_picture = models.ImageField()

    gender = models.CharField(max_length=1, choices=GENDERS)

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)


class StatusUpdate(models.Model):
    content = models.TextField(blank=False)
    thumbnail = models.ImageField()

    creator = models.ForeignKey(UserProfile)

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
