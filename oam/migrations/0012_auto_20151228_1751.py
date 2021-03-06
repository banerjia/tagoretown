# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oam', '0011_auto_20151227_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='corp_url_id',
            field=models.CharField(db_index=True, default='graeters', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(db_index=True, max_length=254),
        ),
    ]
