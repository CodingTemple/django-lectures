from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    # additional classes

    portfolio_site = models.URLField(blank=True) #User doesn't have to fill this out
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank= True)

    def __str__(self):
        return self.user.username
