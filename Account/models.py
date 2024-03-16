from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here. 

class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    RELATIONSHIP_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('R', 'In a Relationship'),
        ('C', 'Complicated'),
        ('W', 'Widowed'),
        ('D', 'Divorced'),
        ('P', 'Separated'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nick_name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='Profile')
    dob = models.DateField(null=True, blank=True)  # Optional date of birth
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    relationship_status = models.CharField(max_length=1, choices=RELATIONSHIP_STATUS_CHOICES, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_of_joined = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self) -> str:
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 
    
    
    
#chat models 



    