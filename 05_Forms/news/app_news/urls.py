from django.urls import path
from .views import NewListView, NewDetailView


urlpatterns = [
    path('news', NewListView.as_view(), name='news'),
    path('news/<int:new_id>', NewDetailView.as_view(), name='new-detail')
]
