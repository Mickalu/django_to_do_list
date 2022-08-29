from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profil

# @receiver(post_save, sender=User)
# def create_profil(sender, instance, created, **kwargs):
#     Profil.objects.create(user=instance)