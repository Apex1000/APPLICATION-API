from django.urls import path,include
from core.views import *

urlpatterns = [
    path('create-company/',CompanyRegistration.as_view(),name="create_company"),
    path('create-location/',LocationRegistration.as_view(),name="create_location"),
    path('create-field/',FieldRegistration.as_view(),name="create_field"),
]