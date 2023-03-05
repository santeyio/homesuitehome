from rest_framework import serializers
from .models import Expenditure, ExpenditureCategory

class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = [
            'created',
            'updated',
            'date',
            'cost',
            'store',
            'description',
            'for_who',
            'category',
            'user',
            'household',
        ]


class ExpenditureCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenditureCategory
        fields = [ 'name' ]
