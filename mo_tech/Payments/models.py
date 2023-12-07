""" Payments models """
from django.db import models
from Customers.models import CustumersModel
from Loans.models import LoansModel

class PaymentsModel(models.Model):
    """ Payments Model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60)
    total_amount = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    status = models.SmallIntegerField(default=1)
    paid_at = models.DateTimeField(auto_now_add=True)
    custumers_id = models.ForeignKey(CustumersModel, on_delete=models.CASCADE)

    class Meta:
        """ Meta class """
        db_table = 'payments_payments'

class PaymentsDetailsModel(models.Model):
    """ PaymentsDetails Model """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    loand_id = models.ForeignKey(LoansModel, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(PaymentsModel, on_delete=models.CASCADE)

    class Meta:
        """ Meta class """
        db_table = 'payments_paymentsdetail'
