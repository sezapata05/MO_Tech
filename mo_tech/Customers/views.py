""" Customers views module """
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from .models import CustumersModel
from .serializers import CustumersSerializer


class ManageCustomersView(APIView):
    """Servicio para crear un cliente"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """ GET METHOD """
        customers = CustumersModel.objects.all()
        serializer = CustumersSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ POST METHOD """
        serializer = CustumersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(status=1)  # Configurando el status como activo
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetCustomerBalanceView(APIView):
    """Servicio para obtener el balance del cliente"""
    permission_classes = [IsAuthenticated]

    def get(self, request, external_id):
        """ GET METHOD """
        try:
            customer = CustumersModel.objects.get(external_id=external_id)
        except CustumersModel.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

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
