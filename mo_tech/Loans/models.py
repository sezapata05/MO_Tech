""" LoansModels module"""
from django.db import models
from Customers.models import CustumersModel

class LoansModel(models.Model):
    """ LoansModel Class """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60)
    status = models.SmallIntegerField(default=1)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    contract_version = models.SmallIntegerField(default=1)
    maximum_payment_date = models.DateTimeField(auto_now=True)
    taken_at = models.DateTimeField(auto_now=True)
    custumers_id = models.ForeignKey(CustumersModel, on_delete=models.CASCADE)
    outstanding = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    class Meta:
        """ MetaClass """
        db_table = 'loans_loan'
