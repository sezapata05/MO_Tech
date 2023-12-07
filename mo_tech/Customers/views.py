""" Customers views module """
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
from .models import CustumersModel
from .serializers import CustumersSerializer

@api_view(['GET', 'POST'])
def manage_customers(request):
    """Servicio para crear un cliente"""
    if request.method == 'GET':
        customers = CustumersModel.objects.all()
        serializer = CustumersSerializer(customers, many=True)
        return Response(serializer.data)

    serializer = CustumersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(status=1)  # Configurando el status como activo
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_customer_balance(request, external_id):
    """Servicio para obtener el balance del cliente"""
    try:
        customer = CustumersModel.objects.get(external_id=external_id)
    except CustumersModel.DoesNotExist:
        return Response({"error": "Custumer not found"}, status=status.HTTP_404_NOT_FOUND)

    print('Esta pasando por acaaa!')

    total_debt = customer.loansmodel_set.filter(status__in=[1, 2]).aggregate(
        total_debt=models.Sum('outstanding')
        )['total_debt'] or 0.0
    available_amount = float(customer.score) - float(total_debt)

    balance_data = {
        "external_id": customer.external_id,
        "score": customer.score,
        "available_amount": available_amount,
        "total_debt": total_debt
    }

    return Response(balance_data, status=status.HTTP_200_OK)
