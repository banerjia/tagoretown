from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.contenttypes.fields \
    import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
import locale

# Create your models here.
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass


class Note(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    isEditable = models.BooleanField(default=True)
    isRemovable = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.title


class Image(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    title = models.CharField(max_length=150)
    image_cdn_url = models.URLField("Image URL", max_length=200)
    notes = GenericRelation(Note)

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=150)
    corp = models.CharField(max_length=255, blank=True)
    corp_url_id = models.CharField(
        max_length=255,
        null=False,
        db_index=True,
        unique=True)
    email = models.EmailField(max_length=254, db_index=True)
    password = models.CharField(max_length=255)
    notes = GenericRelation(Note)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.corp)

    class Meta:
        ordering = ['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'corp', 'email')

    class Meta:
        ordering = ['-date_added']


class Invoice(models.Model):
    customer = models.ForeignKey('Customer')
    number = models.CharField('Invoice #', max_length=50)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    paid = models.BooleanField(default=False)
    void = models.BooleanField(default=False)
    invoice_date = models.DateField()
    due_date = models.DateField(default=None, null=True, blank=True)
    date_paid = models.DateField(default=None, null=True, blank=True)
    notes = GenericRelation(Note)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

    def status(self):
        if(self.paid):
            retval = "Paid"
        elif(self.due_date is not None and
             self.due_date < timezone.now().date()):
            retval = "Overdue"
        else:
            retval = "Unpaid"

        return retval

    def balance_due(self):
        transaction_total = getattr(self, 'transaction_total', None)
        if not transaction_total:
            transaction_total = self.transaction_set.aggregate(
                models.Sum('amount'))['amount__sum'] or 0
        return self.amount - transaction_total


class Transaction(models.Model):
    invoice = models.ForeignKey('Invoice')
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    payment_type = models.CharField(max_length=30, default="Cheque")
    notes = GenericRelation(Note)
    images = GenericRelation(Image)
    date_added = models.DateTimeField("Transaction Date", blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Transaction for {0} on {1:%B %d, %Y}'.format(
            self.invoice.number,
            self.date_added)

    class Meta:
        ordering = ['-date_added']


class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'date_added',
        'invoice_number',
        'invoice_amount',
        'formatted_amount', ]

    def invoice_number(self, obj):
        return obj.invoice.number

    invoice_number.short_description = "Invoice Number"

    def formatted_amount(self, obj):
        return locale.currency(obj.amount, grouping=True)

    formatted_amount.short_description = "Transaction Amount"
    formatted_amount.admin_order_field = "amount"

    def invoice_amount(self, obj):
        return locale.currency(obj.invoice.amount, grouping=True)

    invoice_amount.short_description = "Invoiced Amount"
    invoice_amount.admin_order_field = "invoice__amount"
