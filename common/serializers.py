from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Household, User

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password,
        )

        if not user:
            msg = ('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return

class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
        fields = [ 'name', 'id' ]

class UserSelfSerializer(serializers.ModelSerializer):
    household = HouseholdSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'household',
        ]


class UserFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
        ]
