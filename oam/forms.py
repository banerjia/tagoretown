from django import forms


class InvoiceForm(forms.Form):
    number = forms.CharField(label="Invoice #", max_length=50)
    date_added = forms.DateField(label="Invoice Date")
    amount = forms.DecimalField(label="Amount")
    paid = forms.BooleanField(label="Paid")
