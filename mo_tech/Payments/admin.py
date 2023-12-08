from django.contrib import admin
from .models import PaymentsModel, PaymentsDetailsModel

# Register your models here.
admin.site.register(PaymentsModel)
admin.site.register(PaymentsDetailsModel)