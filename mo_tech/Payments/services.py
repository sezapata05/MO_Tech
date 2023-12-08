""" Service helper """
from django.db import transaction
from django.shortcuts import get_object_or_404
from Loans.models import LoansModel
from Customers.models import CustumersModel
from .models import PaymentsModel, PaymentsDetailsModel

class PaymentService:
    """ PaymentService class """
    @classmethod
    def create_payment(cls, external_id, customer_external_id, loan_external_id, payment_date, total_amount, payment_amount):
        """ create_payment Method """
        customer = get_object_or_404(CustumersModel, external_id=customer_external_id)
        loan = get_object_or_404(LoansModel, external_id=loan_external_id, custumers_id=customer)

        if loan.status != 2 or payment_amount > loan.outstanding:
            raise ValueError("Invalid payment. Check loan status or payment amount.")

        with transaction.atomic():
            payment = PaymentsModel.objects.create(
                external_id=external_id,
                total_amount=total_amount,
                status=1,
                custumers_id=customer
            )

            PaymentsDetailsModel.objects.create(
                amount=payment_amount,
                loand_id=loan,
                payment_id=payment
            )

            loan.outstanding -= payment_amount
            if loan.outstanding == 0:
                loan.status = 4
            else:
                loan.status = 2

            loan.save()

        return payment

    @classmethod
    def get_payments_by_customer(cls, customer_external_id):
        """ get_payments_by_customer Method """
        payments = PaymentsModel.objects.filter(custumers_id__external_id=customer_external_id).prefetch_related('paymentsdetailsmodel_set__loand_id')
        return payments
