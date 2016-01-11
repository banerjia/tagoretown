from django.conf.urls import url

from . import views

app_name = "oam"


urlpatterns = [
    url(r'^invoices/$', views.index, name="invoices_index"),
    url(r'^invoices/new$', views.new, name="invoices_new"),
    url(r'^invoice/(?P<pk>[0-9]+)$', views.detail, name="invoice_detail"),
    url(r'^invoice/(?P<pk>[0-9]+)/edit$', views.edit, name="invoice_edit"),
    url(r'^invoice/(?P<pk>[0-9]+)/new/transaction$',
        views.new_transaction, name="invoice_new_transaction"),
    url(r'^invoice/(?P<pk>[0-9]+)/transaction/(?P<transaction_id>[0-9]+)/edit$',
        views.edit_transaction, name="invoice_edit_transaction"),
    url(r'^invoice/(?P<pk>[0-9]+)/new/note$',
        views.new_note, name="invoice_new_note"),
]
