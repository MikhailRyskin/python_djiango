from django.urls import path
from app_contacts.views import Contacts

urlpatterns = [
    path('', Contacts.as_view(), name='contacts'),
]
