""" serializers module """
from rest_framework import serializers
from .models import PaymentsModel, PaymentsDetailsModel

class PaymentsDetailsSerializer(serializers.ModelSerializer):
    """ PaymentsDetailsSerializer class """
    class Meta:
        """ Meta class """
        model = PaymentsDetailsModel
        fields = '__all__'

class PaymentsSerializer(serializers.ModelSerializer):
    """ PaymentsSerializer class """
    paymentdetailsmodel_set = PaymentsDetailsSerializer(many=True, read_only=True)

    class Meta:
        """ Meta class """
        model = PaymentsModel
        fields = '__all__'
