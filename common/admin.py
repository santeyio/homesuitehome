from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Household

@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            ('Other'),
            {
                'fields': (
                    'household',
                ),
            },
        ),
    )
