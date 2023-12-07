""" URL module """
from django.urls import path
from .views import ManageCustomersView, GetCustomerBalanceView

urlpatterns = [
    path('customers/', ManageCustomersView.as_view(), name='manage_customers'),
    path('balance/<str:external_id>/', GetCustomerBalanceView.as_view(), name='get_customer_balance'),
]
