from django import forms
from .models import Invoice


# class InvoiceForm(forms.Form):
# number = forms.CharField(label="Invoice #", max_length=50)
#    date_added = forms.DateField(label="Invoice Date")
#    amount = forms.DecimalField(label="Amount")
#    paid = forms.BooleanField(label="Paid")


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ['number', 'amount', 'paid',
                  'customer', 'due_date', ]
        localized_fields = ('amount', 'due_date',)
