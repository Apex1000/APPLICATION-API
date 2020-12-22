from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import Location
from .serializers import *
from core.permission import *
from rest_framework.response import Response

class GetLocation(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = SecretaryLocation
    queryset = Location.objects.all()

    def get_queryset(self):
        return self.queryset.filter(secretary = self.request.user)