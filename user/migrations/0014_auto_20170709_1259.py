# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-09 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20170709_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='neworders',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='neworders',
            name='customer_username',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='neworders',
            name='employee_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='neworders',
            name='order_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='neworders',
            name='total_price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
