from django.urls import path
from app_about.views import AboutList

urlpatterns = [
    path('', AboutList.as_view(), name='about_list'),
]
