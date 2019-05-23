from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    phone = models.DecimalField(max_digits=12, decimal_places=0)
    userphoto = models.ImageField(upload_to='profile/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
