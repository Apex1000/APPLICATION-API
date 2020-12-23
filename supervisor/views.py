from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from worker.models import Worker,Activity
from core.models import Field
from .serializers import *
from core.permission import *
from rest_framework.response import Response

class GetFields(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,IsSupervisorUser ]
    serializer_class = SupervisorField
    queryset = Field.objects.all()
    def get_queryset(self):
        return self.queryset.filter(supervisor = self.request.user)