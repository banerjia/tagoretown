# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oam', '0012_auto_20151228_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
