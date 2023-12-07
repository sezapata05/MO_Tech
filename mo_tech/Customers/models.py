""" Custumers models """
from django.db import models

class CustumersModel(models.Model):
    """ Custumers Models for db """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60)
    status = models.SmallIntegerField(default=1)
    score = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    preapproved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ MetaClass """
        db_table = 'customers_customer'
