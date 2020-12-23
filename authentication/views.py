from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from .renderers import UserRenderer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class UserRegistration(generics.GenericAPIView):
    serializer_class = UserCreateSerializer
    renderer_class = (UserRenderer,)

    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(username=user_data['username'])
        token = RefreshToken.for_user(user).access_token
        return Response(user_data, status=status.HTTP_201_CREATED)

class UserLogin(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserLogout(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetails(generics.ListCreateAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserDetails.objects.all()
    def perform_create(self,serializer):
        return serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class IsUserVerified(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        user = {
            'username':self.request.user.username,
            'is_verified': self.request.user.is_verified
        }
        return Response(user, status=status.HTTP_200_OK)

class UserProfile(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    
    def get_queryset(self):
        return self.queryset

class SetNewPasswordAPIView(generics.UpdateAPIView):
        serializer_class = SetNewPasswordSerializer
        model = User
        permission_classes = (permissions.IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                if not self.object.is_verified:
                    self.object.is_verified = True
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)