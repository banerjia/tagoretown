from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Prefetch, Count, Sum
from oam.models import Customer, Invoice, Transaction, Note
from .forms import InvoiceForm, TransactionForm, NoteForm

return_dict = {
    'title': None,
    'customer_name': None,
    'customer_url_id': None,
}


def Http404(request):
    render(request, r'oam/error404.html')


def index(request, customer_url_id):
    qs_invoices_base = Invoice.objects.order_by("-date_added").annotate(
        num_of_transactions=Count('transaction'),
        transaction_total=Sum('transaction__amount')
    ).only(
        'date_added', 'amount', 'number')
    customer = get_object_or_404(
        Customer.objects
        .prefetch_related(
            Prefetch("invoice_set",
                     queryset=qs_invoices_base.filter(paid=True),
                     to_attr="invoices_paid"),
            Prefetch("invoice_set",
                     queryset=qs_invoices_base.filter(paid=False),
                     to_attr="invoices_unpaid")).only('corp'),
        corp_url_id=customer_url_id)

    return_dict.update({
        'title': 'Invoices',
        'customer_name': customer.corp,
        'invoices_paid': customer.invoices_paid[:5],
        'invoices_unpaid': customer.invoices_unpaid[:5],
        'customer_url_id': customer_url_id,
    })
    return render(request, r'oam/index.html', return_dict)


def detail(request, customer_url_id, pk):
    selected_invoice = get_object_or_404(
        Invoice.objects
        .only('invoice_date', 'due_date', 'amount', 'customer__corp')
        .annotate(number_of_notes=Count('notes'))
        .select_related('customer')
        .prefetch_related(
            Prefetch('transaction_set',
                     queryset=Transaction.objects.order_by(
                         "-date_added"),
                     to_attr="transactions")), id=pk)
    return render(request, r'oam/invoice/detail.html', {
        'title': 'Invoice: {0}'.format(selected_invoice.number),
        'browser_title': 'Invoice# {0}'.format(selected_invoice.number),
        'invoice': selected_invoice,
        'related_transactions': selected_invoice.transactions,
        'customer_url_id': selected_invoice.customer.corp_url_id
    })


def edit(request, customer_url_id, pk):
    invoice = Invoice.objects.get(pk=pk)
    form = InvoiceForm(request.POST or None, instance=invoice)
    if(request.POST):
        saved_invoice = form.save(commit=False)

        saved_invoice.paid = bool(form.cleaned_data['date_paid'])

        saved_invoice.save()
        return HttpResponseRedirect(
            reverse("oam:invoice_detail",
                    kwargs={'customer_url_id':
                            saved_invoice.customer.corp_url_id,
                            'pk': pk}))

    return_dict.update({
        'title': 'Edit Invoice# {}'.format(invoice.number),
        'form': form,
        'customer_url_id': customer_url_id,
        'pk': pk
    })
    return render(request, "oam/invoice/edit.html", return_dict)


def new(request, customer_url_id):
    form = InvoiceForm(request.POST or None, initial={
                       'customer': Customer.objects.get(
                           corp_url_id=customer_url_id)})
    if(request.POST):
        if form.is_valid():
            new_invoice = form.save(commit=False)
            new_invoice.balance_due = new_invoice.amount
            new_invoice.save()
            return HttpResponseRedirect(
                reverse("oam:invoice_detail",
                        kwargs={'customer_url_id':
                                new_invoice.customer.corp_url_id,
                                'pk': new_invoice.pk}))

    return_dict.update({
        'title': 'New Invoice',
        'form': form,
        'customer_url_id': customer_url_id
    })
    return render(request, "oam/invoice/new.html", return_dict)


def new_transaction(request, customer_url_id, pk):
    invoice = Invoice.objects.only('number').get(pk=pk)
    form = TransactionForm(request.POST or None)
    if(request.POST):
        invoice.transaction_set.create(
            amount=form.cleaned_data['amount'],
            payment_type=form.cleaned_data['payment_type'])
        invoice.save()
        return HttpResponseRedirect(
            reverse("oam:invoice_detail",
                    kwargs={'customer_url_id':
                            customer_url_id,
                            'pk': pk}))

    return_dict.update({
        'title': 'New Transaction for Invoice# {}'.format(invoice.number),
        'form': form,
        'customer_url_id': customer_url_id,
        'super_template': "oam/modal_layout.html",
        'post_url': reverse("oam:invoice_new_transaction",
                            kwargs={'customer_url_id': customer_url_id,
                                    'pk': pk})
    })
    return render(request, 'oam/transaction/new.html', return_dict)


def edit_transaction(request, customer_url_id, pk):
    pass


def new_note(request, customer_url_id, pk):
    invoice = Invoice.objects.only('number').get(pk=pk)
    form = NoteForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            invoice.notes.create(text=form.cleaned_data['text'])
            invoice.save()
            return HttpResponseRedirect(
                reverse("oam:invoice_detail",
                        kwargs={'customer_url_id':
                                customer_url_id,
                                'pk': pk}))

    return_dict.update({
        'title': 'New Note for Invoice# {}'.format(invoice.number),
        'form': form,
        'customer_url_id': customer_url_id,
        'super_template': "oam/modal_layout.html",
        'post_url': reverse("oam:invoice_new_note",
                            kwargs={'customer_url_id': customer_url_id,
                                    'pk': pk})
    })
    return render(request, "oam/note/new.html", return_dict)


def notes(request, customer_url_id, pk):
    selected_invoice = Invoice.objects.only('number').prefetch_related(
        Prefetch('notes',
                 queryset=Note.objects.only(
                     'text', 'date_added')
                 .order_by("-date_added"))) \
        .get(pk=pk)
    return_dict.update({
        'title': 'Notes for Invoice# {}'.format(selected_invoice.number),
        'notes': selected_invoice.notes.all(),
        'customer_url_id': customer_url_id,
        'super_template': "oam/modal_layout.html",
    })

    return render(request, "oam/note/list.html", return_dict)
