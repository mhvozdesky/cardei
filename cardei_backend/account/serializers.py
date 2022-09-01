from djoser.serializers import UserSerializer, UserCreateSerializer, UserCreatePasswordRetypeSerializer
from djoser.conf import settings

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from account.models import CardeiUser
from notification.notification import EMAIL_IS_USED, INCORRECT_CREDITS
from django.contrib.auth import authenticate


class CardeiUserSerializer(serializers.ModelSerializer):
    """Serialization for user's internal display"""

    class Meta:
        model = CardeiUser
        fields = [
            'id',
            'last_login',
            'email'
        ]


class CardeiUserCreateSerializer(UserCreatePasswordRetypeSerializer):
    """Serialization to create user"""

    email = serializers.EmailField(
        required=True,
        max_length=100,
        validators=[
           UniqueValidator(
               queryset=CardeiUser.objects.all(),
               message=EMAIL_IS_USED,
           )
        ])

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        return super().create(validated_data)

    class Meta:
        model = CardeiUser
        fields = tuple(CardeiUser.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            'password'
        )


class CardeiUserAuthSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100, required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        email = data['email']
        password = data['password']
        user_auth = authenticate(
            request=self.context['request'],
            email=email,
            password=password)

        if user_auth is None:
            raise serializers.ValidationError(INCORRECT_CREDITS)
        data['user_auth'] = user_auth
        return data
