from django.db import models

from django.contrib.auth.models import AbstractUser

class Household(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(AbstractUser):
    household = models.ForeignKey(Household, on_delete=models.SET_NULL, null=True, blank=True)
