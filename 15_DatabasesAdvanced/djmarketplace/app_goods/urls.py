from django.urls import path
from .views import ItemListView, ItemDetailView, StatisticsView


urlpatterns = [
    path('items/', ItemListView.as_view(), name='items'),
    path('items/<int:pk>', ItemDetailView.as_view(), name='item_detail'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]