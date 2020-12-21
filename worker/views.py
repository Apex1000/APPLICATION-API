from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from worker.models import Worker,Activity
from .serializers import *
from rest_framework.response import Response

class WorkerFields(generics.GenericAPIView):
    serializer_class = WorkerFieldSerializer
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        worker_data = serializer.data
        return Response(worker_data,status=status.HTTP_201_CREATED)

class AllActivity(generics.ListAPIView):
    serializer_class = ActivitiesSerializer
    queryset = Activity.objects.all()
    
    def get_queryset(self):
        return self.queryset

class ActivityUpdate(RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitiesSerializer
    queryset = Activity.objects.all()
    lookup_field = "id"
    
    def get_queryset(self):
        return self.queryset