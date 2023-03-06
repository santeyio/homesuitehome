from django.contrib import admin
from .models import Expenditure, ExpenditureCategory, Beneficiary

@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    pass

@admin.register(ExpenditureCategory)
class ExpenditureCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    pass
