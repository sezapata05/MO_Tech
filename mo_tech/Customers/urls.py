""" URL module """
from django.urls import path
from .views import manage_customers, get_customer_balance


urlpatterns = [
    path(r'customers/', manage_customers, name='manage_customers'),
    path(r'balance/<str:external_id>/', get_customer_balance, name='get_customer_balance'),
]
