from rest_framework import serializers
from authentication.models import Company
from django.contrib import auth

class CompanyRegistration(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'