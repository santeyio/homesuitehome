from django.db import models

from django.contrib.auth.models import AbstractUser

class Household(models.Model):
    name = models.CharField(max_len=200)

class User(AbstractUser):
    pass
    household = models.ForeignKey(Household, on_delete=models.SET_NULL)
