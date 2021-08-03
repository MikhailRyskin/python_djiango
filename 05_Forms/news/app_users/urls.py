from django.urls import path
from .views import AnotherLoginView, AnotherLogoutView, register_view, AccountDetailView

urlpatterns = [
    path('login', AnotherLoginView.as_view(), name='login'),
    path('logout', AnotherLogoutView.as_view(), name='logout'),
    path('register', register_view, name='register'),
    path('account/<int:pk>', AccountDetailView.as_view(), name='account'),
]
