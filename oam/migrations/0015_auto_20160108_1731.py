# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 22:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('oam', '0014_auto_20151229_0215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-date_added']},
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='balance_due',
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 8, 22, 31, 28, 537266, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='void',
            field=models.BooleanField(default=False),
        ),
    ]
