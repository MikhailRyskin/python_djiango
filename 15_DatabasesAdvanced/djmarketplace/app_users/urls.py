from django.urls import path
from .views import AnotherLoginView, AnotherLogoutView, register_view, AccountDetailView, balance_view, CartView

urlpatterns = [
    path('login', AnotherLoginView.as_view(), name='login'),
    path('logout', AnotherLogoutView.as_view(), name='logout'),
    path('register', register_view, name='register'),
    path('account/<int:pk>', AccountDetailView.as_view(), name='account'),
    path('account/<int:pk>/add_balance/', balance_view, name='add_balance'),
    path('account/<int:pk>/cart/', CartView.as_view(), name='cart'),
]