from django.shortcuts import render
from django.contrib.auth import login

from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .serializers import AuthSerializer, HouseholdSerializer
from .models import Household

class LoginView(KnoxLoginView):
    #  serializer_class = AuthSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

class HouseholdViewSet(viewsets.ModelViewSet):
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializer
