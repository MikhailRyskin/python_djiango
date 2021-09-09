from django.urls import path
from app_news.views import NewsItemList, NewsItemDetailView

urlpatterns = [
    path('', NewsItemList.as_view(), name='newsitem_list'),
    path('<int:pk>', NewsItemDetailView.as_view(), name='newsitem_detail'),
]