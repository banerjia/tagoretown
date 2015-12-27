from django.contrib import admin
from .models \
    import Customer, \
    CustomerAdmin, \
    Invoice, \
    Transaction, \
    TransactionAdmin, \
    Image
# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Image)
