""" serializers module """
from rest_framework import serializers
from .models import PaymentsModel, PaymentsDetailsModel


class PaymentsDetailsModelSerializer(serializers.ModelSerializer):
    """ PaymentsDetailsModelSerializer """
    class Meta:
        """ Meta Class """
        model = PaymentsDetailsModel
        fields = '__all__'

class PaymentsModelSerializer(serializers.ModelSerializer):
    """ PaymentsModelSerializer """
    paymentsdetailsmodel_set = PaymentsDetailsModelSerializer(many=True, read_only=True)

    class Meta:
        """ Meta Class """
        model = PaymentsModel
        fields = '__all__'
