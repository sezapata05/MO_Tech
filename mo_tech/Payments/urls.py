""" URL module """
from django.urls import path
from .views import create_payment, get_payments_by_customer

urlpatterns = [
    path('create_payment/', create_payment, name='create_payment'),
    path('get_payments_by_customer/<str:customer_external_id>/', get_payments_by_customer, name='get_payments_by_customer'),
]
