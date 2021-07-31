from django.urls import path
from .views import AnotherLoginView, AnotherLogoutView

urlpatterns = [
    path('login', AnotherLoginView.as_view(), name='login'),
    path('logout', AnotherLogoutView.as_view(), name='logout'),
]
