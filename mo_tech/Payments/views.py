""" Payments views module """
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.parsers import JSONParser
from .services import PaymentService
from .serializers import PaymentsModelSerializer

@csrf_exempt
@require_POST
def create_payment(request):
    """ POST METHOD """
    try:
        data = JSONParser().parse(request)
        serializer = PaymentsModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        payment = PaymentService.create_payment(
            external_id=serializer.validated_data['external_id'],
            customer_external_id=serializer.validated_data['custumers_id'].external_id,
            loan_external_id=serializer.validated_data['paymentsdetailsmodel'][0]['loand_id'],
            payment_date=serializer.validated_data['paid_at'],
            total_amount=serializer.validated_data['total_amount'],
            payment_amount=serializer.validated_data['paymentsdetailsmodel'][0]['amount']
        )

        response_serializer = PaymentsModelSerializer(payment)
        return JsonResponse(response_serializer.data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def get_payments_by_customer(request, customer_external_id):
    """ GET METHOD """
    try:
        payments = PaymentService.get_payments_by_customer(customer_external_id)
        response_serializer = PaymentsModelSerializer(payments, many=True)
        return JsonResponse({'payments': response_serializer.data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
