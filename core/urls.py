from django.urls import path,include
from core.views import *

urlpatterns = [
    path('create-location/',LocationRegistration.as_view(),name="create_location"),
    path('create-field/',FieldRegistration.as_view(),name="create_field"),
    path('get-fields/',GetFields.as_view(),name="get-fields"),
    path('get-locations/',GetLocation.as_view(),name="get-locations"),
    path('activity/<int:id>/',ActivitiesAPI.as_view(),name='activity'),
]