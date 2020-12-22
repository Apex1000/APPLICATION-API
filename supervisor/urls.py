from django.urls import path, include
from supervisor.views import *

urlpatterns = [
    path('',GetFields.as_view(),name='supervisor'),
]