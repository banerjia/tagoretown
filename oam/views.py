from django.shortcuts import render, get_object_or_404
from oam.models import Invoice


# Create your views here.
def index(request, customer_url_id):
    invoices = Invoice.objects.filter(
        customer__corp_url_id__iexact=customer_url_id).order_by('-date_added')
    return render(request, r'oam/index.html', {
        'title': 'Homepage',
        'invoice_list': invoices,
        'customer_url_id': customer_url_id,
    })


def detail(request, customer_url_id, pk):
    selected_invoice = get_object_or_404(Invoice, id=pk)
    return render(request, r'oam/detail.html', {
        'title': ' '.join(['Invoice Number', selected_invoice.number]),
        'invoice': selected_invoice,
        'related_transactions': selected_invoice
        .transaction_set
        .order_by("-date_added"),
        'customer': selected_invoice.customer,
    })
