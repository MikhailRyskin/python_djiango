from django.urls import path
from .views import ShopListView

urlpatterns = [
    path('shops', ShopListView.as_view(), name='shops'),
    ]