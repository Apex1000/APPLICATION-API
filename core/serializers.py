from rest_framework import serializers
from .models import *
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

class CompanyRegistration(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class LocationRegistration(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class FieldRegistration(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class GetField(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class GetLocation(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'