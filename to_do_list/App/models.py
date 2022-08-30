from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'profile_image', blank=True, null=True)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    state = models.BooleanField(default=False)