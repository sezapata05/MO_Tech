""" serializers module """
from rest_framework import serializers
from .models import CustumersModel

class CustumersSerializer(serializers.ModelSerializer):
    """ CustumersSerializer class """

    class Meta:
        """ Metaclass """
        model = CustumersModel
        fields = ['external_id', 'status', 'score', 'preapproved_at']
