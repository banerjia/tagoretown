from django.shortcuts import render, get_object_or_404
from oam.models import Customer, Invoice

return_dict = {
    'title': None,
    'customer_name': None,
}

# Create your views here.


def index(request, customer_url_id):
    customer = get_object_or_404(
        Customer, corp_url_id=customer_url_id)
    invoices = customer.invoice_set.order_by('-date_added')
    return_dict.update({
        'customer_name': customer.corp,
        'invoices_paid': invoices.filter(paid=True)[:5],
        'invoices_unpaid': invoices.filter(paid=False)[:5],
        'customer_url_id': customer_url_id,
    })
    return render(request, r'oam/index.html', return_dict)


def detail(request, customer_url_id, pk):
    selected_invoice = get_object_or_404(Invoice, id=pk)
    return render(request, r'oam/detail.html', {
        'title': 'Invoice: {0}'.format(selected_invoice.number),
        'browser_title': 'Invoice# {0}'.format(selected_invoice.number),
        'invoice': selected_invoice,
        'invoice_notes': selected_invoice.notes.all(),
        'related_transactions': selected_invoice.transaction_set
        .order_by("-date_added"),
        'customer': selected_invoice.customer,
    })
