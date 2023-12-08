""" Payments models """
from django.db import models
from Loans.models import LoansModel
from Customers.models import CustumersModel

class PaymentsModel(models.Model):
    """ Payment model Class """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60)
    total_amount = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    status = models.SmallIntegerField(default=1)
    paid_at = models.DateTimeField(auto_now_add=True)
    custumers_id = models.ForeignKey(CustumersModel, on_delete=models.CASCADE)

    class Meta:
        """ Meta Class """
        db_table = 'payments_payments'

class PaymentsDetailsModel(models.Model):
    """ Payment Detail model class """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    loan_id = models.ForeignKey(LoansModel, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(PaymentsModel, on_delete=models.CASCADE, related_name='paymentsdetailsmodel_set')

    class Meta:
        """ Meta Class """
        db_table = 'payments_paymentsdetail'
