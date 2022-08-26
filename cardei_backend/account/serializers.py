from djoser.serializers import UserSerializer, UserCreateSerializer, UserCreatePasswordRetypeSerializer
from djoser.conf import settings

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from account.models import CardeiUser
from notification.notification import EMAIL_IS_USED, PASSWORD_MISMATCH


# class CardeiUserCreateSerializer(UserCreatePasswordRetypeSerializer):
#     """Serialization to create user"""
#
#     email = serializers.EmailField(
#         required=True,
#         max_length=100,
#         validators=[
#            UniqueValidator(
#                queryset=CardeiUser.objects.all(),
#                message=EMAIL_IS_USED,
#            )
#         ])
#
#     class Meta:
#         model = CardeiUser
#         fields = tuple(CardeiUser.REQUIRED_FIELDS) + (
#             settings.LOGIN_FIELD,
#             settings.USER_ID_FIELD,
#             "password",
#         )


# class CardeiUserUpdateSerializer(UserSerializer):
#     """Serialization to change user data"""
#
#     email = serializers.EmailField(
#         required=True,
#         max_length=100,
#         validators=[
#            UniqueValidator(
#                queryset=CardeiUser.objects.all(),
#                message=EMAIL_IS_USED,
#            )
#         ])
#
#     class Meta:
#         model = CardeiUser
#         fields = tuple(CardeiUser.REQUIRED_FIELDS) + (
#             settings.USER_ID_FIELD,
#             settings.LOGIN_FIELD,
#             'first_name',
#             'last_name',
#             'middle_name',
#             'email',
#             'avatar',
#         )
#         read_only_fields = (settings.LOGIN_FIELD,)


class CardeiUserSerializer(serializers.ModelSerializer):
    """Serialization for user's internal display"""

    class Meta:
        model = CardeiUser
        fields = '__all__'


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

    # re_password = serializers.CharField(style={"input_type": "password"})

    # def validate(self, attrs):
    #     self.fields.pop("re_password", None)
    #     re_password = attrs.pop("re_password")
    #     attrs = super().validate(attrs)
    #
    #     if attrs["password"] == re_password:
    #         return attrs
    #     else:
    #         raise ValidationError({'re_password': [PASSWORD_MISMATCH]})

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
