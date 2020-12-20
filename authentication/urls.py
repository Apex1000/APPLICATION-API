from django.urls import path,include
from authentication.views import *
from rest_framework_simplejwt.views import (TokenRefreshView,)

urlpatterns = [
    path('register/', UserRegistration.as_view(), name="register"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/',UserLogout.as_view(),name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-details/',UserDetails.as_view(),name='user_details'),
]