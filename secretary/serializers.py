from rest_framework import serializers
from core.models import Location,Field
from django.contrib import auth

class SecretaryLocationAll(serializers.ModelSerializer):
    location = serializers.StringRelatedField(many=True)
    class Meta:
        model = Location
        fields = ('location_name','location')