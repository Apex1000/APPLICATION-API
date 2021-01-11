from django.urls import path,include
from superadmin.views import *

urlpatterns = [
    path('create-company/',CompanyRegistration.as_view(),name="create_company"),
]