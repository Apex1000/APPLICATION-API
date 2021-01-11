from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from core.permission import *
from rest_framework.response import Response

class LocationRegistration(generics.GenericAPIView):
    serializer_class = LocationRegistration
    permission_classes = (permissions.IsAuthenticated,IsAdminUser)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        location_data = serializer.data
        return Response(location_data,status=status.HTTP_201_CREATED)

class FieldRegistration(generics.GenericAPIView):
    serializer_class = FieldRegistration
    permission_classes = (permissions.IsAuthenticated,IsAdminUser)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        field_data = serializer.data
        return Response(field_data,status=status.HTTP_201_CREATED)

class GetLocation(generics.ListAPIView):
    serializer_class = GetLocation
    permission_classes = (permissions.IsAuthenticated,IsAdminUser)
    queryset = Field.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(secretary=self.request.user)

class GetFields(generics.ListAPIView):
    serializer_class = GetField
    permission_classes = (permissions.IsAuthenticated,IsAdminUser)
    queryset = Field.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(secretary=self.request.user)

class ActivitiesAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = AdminActivitiesSerializer
    permission_classes = (permissions.IsAuthenticated,IsAdminUser)
    queryset = Activity.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset