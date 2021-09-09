from django.urls import path
from app_housings.views import HousingList, HousingDetailView

urlpatterns = [
    path('', HousingList.as_view(), name='housing_list'),
    path('<int:pk>', HousingDetailView.as_view(), name='housing_detail'),
]