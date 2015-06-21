from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="custom_user_profile")
    # custom fields for user
    nick_name = models.CharField(max_length=100)