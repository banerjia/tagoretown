from django.conf.urls import url

from . import views

app_name = "oam"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<pk>[0-9]+)/detail$', views.detail, name="detail"),
    url(r'^new$', views.new_invoice, name="new_invoice"),
    url(r'^(?P<pk>[0-9]+)/edit$', views.edit_invoice, name="edit_invoice"),
]
