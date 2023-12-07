""" serializers module """
from rest_framework import serializers
from Customers.serializers import CustumersSerializer
from Customers.models import CustumersModel
from .models import LoansModel

class LoansModelSerializer(serializers.ModelSerializer):
    """ LoansModelSerializer class """
    custumers_id = CustumersSerializer()

    class Meta:
        """ Meta Class """
        model = LoansModel
        fields = ['external_id', 'custumers_id', 'amount', 'outstanding', 'status']

    def create(self, validated_data):
        """ create method for Loand Serializer """
        customer_data = validated_data.pop('custumers_id')
        external_id = customer_data['external_id']

        customers = CustumersModel.objects.filter(external_id=external_id)

        if customers.exists():
            customer = customers.first()
            customer_serializer = CustumersSerializer(instance=customer, data=customer_data)
            customer_serializer.is_valid(raise_exception=True)
            customer_serializer.save()

            # Create the loan with the existing customer instance
            loan_data = {**validated_data, 'custumers_id': customer}
            loan = LoansModel.objects.create(**loan_data)
            return loan

        raise serializers.ValidationError("Cannot create loan without an existing customer.")
