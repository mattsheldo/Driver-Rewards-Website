from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#class Driver(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    username = models.CharField(max_length=128)
#    ID = models.IntegerField
#    points = models.IntegerField
    
#class Sponsor(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    username = models.CharField(max_length=128)
#    ID = models.IntegerField

#class Admin(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    username = models.CharField(max_length=128)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if not created:
#        Driver.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
