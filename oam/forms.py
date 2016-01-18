from django import forms
from .models import Invoice, Note, Transaction


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ['number', 'amount', 'paid',
                  'customer', 'due_date', 'date_paid', ]
        localized_fields = ('amount', 'due_date', )


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ['amount', 'payment_type', ]

        localized_fields = ('amount', 'date_added', )


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['text', ]

        labels = {
            'text': 'Notes',
        }
