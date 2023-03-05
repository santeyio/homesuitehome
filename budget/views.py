from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Expenditure, ExpenditureCategory
from .serializers import ExpenditureSerializer, ExpenditureCategorySerializer
from .exceptions import HouseholdException

class ExpenditureViewSet(viewsets.ModelViewSet):
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer

    def list(self, request):
        household = request.user.household
        if not household:
            raise HouseholdException
        qs = Expenditure.objects.filter(household=household)
        s = ExpenditureSerializer(qs, many=True)
        return Response(serializer.data)

class ExpenditureCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenditureCategory.objects.all()
    serializer_class = ExpenditureCategorySerializer
