from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from core.permission import *
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
