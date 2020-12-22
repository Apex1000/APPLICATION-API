from rest_framework import serializers
from core.models import Location
from django.contrib import auth

class SecretaryLocation(serializers.ModelSerializer):
    user = serializers.CharField(source='secretary.username',read_only=True)
    class Meta:
        model = Location
        fields = ('user','name')