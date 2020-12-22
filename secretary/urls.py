from django.urls import path, include
from secretary.views import *
urlpatterns = [
    path('',GetLocation.as_view(),name='secretary'),
]