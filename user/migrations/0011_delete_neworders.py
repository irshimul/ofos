# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-09 12:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_completedorders_employee_neworders'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewOrders',
        ),
    ]