from django.db import models
from common.models import User, Household

class Store(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Tag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)


class Ingredient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    sources = models.ManyToManyField(Store)
    in_stock = models.BooleanField(default=False)
    to_buy = models.BooleanField(default=False)
    recipes = models.ManyToManyField(Recipe)


class Package(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    package = models.CharField(max_length=200) # e.g. 12oz can, 32oz bottle, bag, etc
    quantity = models.IntegerField(default=0)
    purchase_date = models.DateField(null=True, blank=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
