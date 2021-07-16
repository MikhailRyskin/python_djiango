from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('1/', views.advertisement_detail_1, name='advertisement_detail_1'),
    path('2/', views.advertisement_detail_2, name='advertisement_detail_2'),
    path('3/', views.advertisement_detail_3, name='advertisement_detail_3'),
    path('4/', views.advertisement_detail_4, name='advertisement_detail_4'),
    path('5/', views.advertisement_detail_5, name='advertisement_detail_5')
]
