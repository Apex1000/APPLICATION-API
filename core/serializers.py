from rest_framework import serializers
from .models import *
from django.contrib import auth

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