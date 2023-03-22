from rest_framework import serializers
from .models import Expenditure, ExpenditureCategory, Beneficiary
from common.serializers import HouseholdSerializer
from common.models import Household

class ExpenditureCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenditureCategory
        fields = [ 'id', 'name' ]

class ExpenditureSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=ExpenditureCategory.objects.all())
    household = serializers.PrimaryKeyRelatedField(queryset=Household.objects.all())
    beneficiary = serializers.PrimaryKeyRelatedField(queryset=Beneficiary.objects.all())

    class Meta:
        model = Expenditure
        fields = [
            'id',
            'created',
            'updated',
            'date',
            'cost',
            'store',
            'description',
            'category',
            'beneficiary',
            'user',
            'household',
        ]
        read_only_fields = [
            'id',
            'created',
            'updated',
            'household',
        ]

class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = [ 'id', 'name' ]
