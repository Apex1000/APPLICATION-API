from django.urls import path,include
from .views import *
urlpatterns = [
    path('workers-field',WorkerFields.as_view(),name="workers-field"),
    path('activities',AllActivity.as_view(),name='activity'),
    path('activities/<int:id>/',ActivityUpdate.as_view(),name='activity'),
]