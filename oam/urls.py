from django.conf.urls import url

from . import views

app_name = "oam"
urlpatterns = [
    url(r'^invoices/$', views.index, name="index"),
    url(r'^invoices/new$', views.new, name="new"),
    url(r'^invoice/(?P<pk>[0-9]+)$', views.detail, name="invoice_detail"),
    url(r'^invoice/(?P<pk>[0-9]+)/edit$', views.edit, name="invoice_edit"),
]
