from rest_framework import serializers
from .models import Expenditure, ExpenditureCategory, Beneficiary
from common.serializers import HouseholdSerializer, UserFlatSerializer
from common.models import Household

class ExpenditureCategorySerializer(serializers.ModelSerializer):
    created_by = UserFlatSerializer()
    last_updated_by = UserFlatSerializer()

    class Meta:
        model = ExpenditureCategory
        fields = [
            'id',
            'name',
            'created_by',
            'last_updated_by',
        ]
        read_only_fields = [ 'id', 'created_by', 'last_updated_by' ]

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
        read_only_fields = [ 'id' ]
