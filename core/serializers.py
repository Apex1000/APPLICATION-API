from rest_framework import serializers
from .models import *
from django.contrib import auth
from worker.models import Activity

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

class AdminActivitiesSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    field = serializers.CharField(source='field.field_name',read_only=True)
    class Meta:
        model = Activity
        fields = ('id','activity','created','user','field')
