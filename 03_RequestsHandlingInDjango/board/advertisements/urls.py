from django.urls import path
from . import views

urlpatterns = [
    path('', views.Advertisements.as_view(), name='advertisement_list'),
]
