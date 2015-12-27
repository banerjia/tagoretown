# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('oam', '0010_auto_20151225_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=150)),
                ('image_cdn_url', models.URLField(verbose_name='Image URL')),
                ('notes', models.TextField(blank=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.RemoveField(
            model_name='transactionimage',
            name='transaction',
        ),
        migrations.DeleteModel(
            name='TransactionImage',
        ),
    ]
