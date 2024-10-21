from django.db import models
from django.contrib.auth.models import User
import os


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/',null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def remove_profile_image(self):
        if self.profile_image:
            if os.path.isfile(self.profile_image.path):
                os.remove(self.profile_image.path)
            self.profile_image = None
            self.save()
