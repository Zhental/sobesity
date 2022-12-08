from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# class Users(models.Model):
#     id = models.AutoField()
#     first_name = models.CharField(max_length=25)
#     first_name = models.CharField(max_length=25)
#     email = models.EmailField(max_length=50, null = False)
#     password = models.CharField(max_length=10, null = False)
#     registration_data = models.DateField()
    
class Technogoly(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=25)
        
# class Tests(models.Model):
#     id = models.AutoField()
#     name = models.CharField(max_length=25)
#     difficulty_level = models.CharField(max_length=25)
#     technogoly_id = models.ForeignKey(Technogoly.id)
    
# class Users_Tests(models.Model):
#     id = models.AutoField()
#     user_id = models.ForeignKey(User.id)
#     test_id = models.ForeignKey(User.id)
    
# class Interviews(models.Model):
#     id = models.AutoField()
#     interviewer_id = models.ForeignKey(Users.id)
#     interviewee_id = models.ForeignKey(Users.id)
#     technogoly_id = models.ForeignKey(Technogoly.id)
#     zoomlink = models.CharField(max_length=30)
#     rating_interviewer = models.IntegerField()
#     rating_interviewee = models.IntegerField()
    
class Fields(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=30)
    technogoly_id = models.ForeignKey(Technogoly.id)