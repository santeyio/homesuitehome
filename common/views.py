from django.shortcuts import render
from django.contrib.auth import login

from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
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


@api_view(['GET'])
def check_if_logged_in(request):
    return Response({'success': True}, status=200)
