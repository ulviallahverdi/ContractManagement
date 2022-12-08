from django.contrib import admin
from .models import *

admin.site.register(ContractType)
admin.site.register(PaymentTerms)
admin.site.register(Contract)
admin.site.register(TerminationTerms)
admin.site.register(Department)
admin.site.register(Status)
admin.site.register(Currency)


# Register your models here.