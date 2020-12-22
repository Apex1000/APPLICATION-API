from rest_framework import serializers
from .models import *

class WorkerFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class AllActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id','activity','field')

class ActivitiesSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    field = serializers.CharField(source='field.name',read_only=True)
    class Meta:
        model = Activity
        fields = ('id','activity','created','user','field')
