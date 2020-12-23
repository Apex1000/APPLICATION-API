from rest_framework import serializers
from core.models import Field
from django.contrib import auth

class SupervisorField(serializers.ModelSerializer):
    user = serializers.CharField(source='supervisor.username',read_only=True)
    class Meta:
        model = Field
        fields = ('user','field_name')