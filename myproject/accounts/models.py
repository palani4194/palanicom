from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    description = models.CharField(max_length=100, default='Enter description')
    city = models.CharField(max_length=100, default='mumbai')
    website = models.URLField(default='www.yourweb.com')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)


    def __str__(self):
        return self.user.username

# if once you create user and after saved it will create new UserProfile

def create_UserProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


# signals
post_save.connect(create_UserProfile, sender=User)
