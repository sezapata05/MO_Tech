""" Loans views module """
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Customers.models import CustumersModel
from .models import LoansModel
from .serializers import LoansModelSerializer


class LoansCreateAPIView(APIView):
    """ API View class """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """ POST METHOD """
        serializer = LoansModelSerializer(data=request.data)
        if serializer.is_valid():

            serializer.validated_data['status'] = 2  # STATUS_ACTIVE

            loan = serializer.save()
            return Response(LoansModelSerializer(loan).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoansByCustomerAPIView(APIView):
    """ API View class """
    permission_classes = [IsAuthenticated]

    def get(self, request, customer_external_id):
        """ GET METHOD """
        try:
            customers = CustumersModel.objects.filter(external_id=customer_external_id)

            if customers.exists():
                customer = customers.first()
                loans = LoansModel.objects.filter(custumers_id_id=customer)
                serializer = LoansModelSerializer(loans, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Error: {e}")
            return Response(
                {"error": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
