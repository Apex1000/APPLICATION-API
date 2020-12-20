from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import *
from rest_framework.response import Response

class CompanyRegistration(generics.GenericAPIView):
    serializer_class = CompanyRegistration

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        company_data = serializer.data
        return Response(company_data,status=status.HTTP_201_CREATED)

class LocationRegistration(generics.GenericAPIView):
    serializer_class = LocationRegistration

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        location_data = serializer.data
        return Response(location_data,status=status.HTTP_201_CREATED)

class FieldRegistration(generics.GenericAPIView):
    serializer_class = FieldRegistration

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        field_data = serializer.data
        return Response(field_data,status=status.HTTP_201_CREATED)