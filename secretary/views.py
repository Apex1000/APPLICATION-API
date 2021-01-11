from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import Location, Field
from authentication.models import User
from .serializers import *
from core.permission import *
from core.permission import IsSecretaryUser
from rest_framework.response import Response

class GetLocation(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,IsSecretaryUser]
    serializer_class = SecretaryLocationAll
    queryset = Location.objects.all()

    def get_queryset(self):
        return self.queryset.filter(secretary = self.request.user)

class Demo(views.APIView):
    def post(self,request):
        data = request.data
        d = {
            'user':(self.request.user.company.username)
        }
        return Response(d,status=status.HTTP_201_CREATED)