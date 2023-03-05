from django.db import models
from common.models import User, Household

class ExpenditureCategory(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Expenditure(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    for_who = models.CharField(max_length=200)
    category = models.ForeignKey(ExpenditureCategory, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
