""" loans URL module """
from django.urls import path
from .views import LoansByCustomerAPIView, LoansCreateAPIView

urlpatterns = [
    path('create_loan/', LoansCreateAPIView.as_view(), name='create_loan'),
    path(
        'get_loans/<str:customer_external_id>/',
        LoansByCustomerAPIView.as_view(),
        name='get_loans_by_customer'
        ),
]
