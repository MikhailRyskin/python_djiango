from django.urls import path
from . import views

urlpatterns = [
    path('', views.Contacts.as_view(), name='contacts'),
]
