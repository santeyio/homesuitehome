from django.contrib import admin
from .models import Expenditure, ExpenditureCategory

@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    pass

@admin.register(ExpenditureCategory)
class ExpenditureCategoryAdmin(admin.ModelAdmin):
    pass
