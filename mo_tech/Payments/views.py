""" Views module """
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.parsers import JSONParser
from Loans.models import LoansModel
from .serializers import PaymentsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class PaymentsView(View):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = PaymentsSerializer(data=data)

        if serializer.is_valid():
            loan_external_id = data['loan_external_id']
            total_amount = data['total_amount']

            loan = LoansModel.objects.get(external_id=loan_external_id)
            if total_amount > loan.outstanding:
                return JsonResponse({'error': 'El pago es superior a la deuda'}, status=400)

            payment = serializer.save()
            PaymentsDetailsModel.objects.create(
                amount=data['payment_amount'],
                loand_id=loan,
                payment_id=payment
            )

            loan.outstanding -= data['payment_amount']
            loan.save()

            return JsonResponse({'success': 'Pago creado exitosamente'}, status=201)
        return JsonResponse(serializer.errors, status=400)

    # def get(self, request):
    #     customer_external_id = request.GET.get('customer_external_id')
    #     loan_external_id = request.GET.get('loan_external_id')

    #     payments = PaymentsModel.objects.filter(
    #         custumers_id__external_id=customer_external_id,
    #         paymentdetailsmodel__loand_id__external_id=loan_external_id
    #     ).select_related('custumers_id').prefetch_related('paymentdetailsmodel_set')

    #     serializer = PaymentsSerializer(payments, many=True)

    #     return JsonResponse({'payments': serializer.data}, status=200)
