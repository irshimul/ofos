# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20170514_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='food',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
