import os
import csv
from dateutil.parser import parse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from common.models import User
from .models import Expenditure, ExpenditureCategory, Beneficiary
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


class LoadTestData():
    def __init__(self):
        self.caleb = User.objects.get(email='santeyio@gmail.com')
        self.amy = User.objects.get(email='ereabraham7@gmail.com')
        self.household = self.caleb.household

    def get_or_create_category(self, category_name):
        try:
            category = ExpenditureCategory.objects.get(household=self.household, name=category_name)
        except ExpenditureCategory.DoesNotExist:
            category = ExpenditureCategory(
                household=self.household,
                name=category_name,
                created_by=self.caleb,
            )
            category.save()
        return category

    def get_or_create_bene(self, bene_name):
        try:
            bene = Beneficiary.objects.get(household=self.household, name__iexact=bene_name.lower().strip())
        except Beneficiary.DoesNotExist:
            bene = Beneficiary(
                household=self.household,
                name=bene_name,
            )
            bene.save()
        return bene

    def run(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(base_dir, 'fixtures/sample_expenditures.csv')
        expenditures = []
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for i, row in enumerate(reader):
                if (row[0] != ''):
                    try:
                        cost = float(row[1])
                    except ValueError:
                        print(f'--- ERROR on row {i}: {row[1]}')
                        cost = 0.0

                    date = parse(row[0])
                    store = row[2]
                    desc = row[3]
                    user = self.amy if row[4].lower().strip() == 'amy' else self.caleb
                    beneficiary = self.get_or_create_bene(row[5])
                    category = self.get_or_create_category(row[6])
                    e = Expenditure(
                        date=date,
                        cost=cost,
                        store=store,
                        description=desc,
                        beneficiary=beneficiary,
                        category=category,
                        user=user,
                        household=self.household,
                    )
                    e.save()
