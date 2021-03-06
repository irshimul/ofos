# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_restaurent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('time_needed', models.DurationField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_users_rated', models.IntegerField()),
                ('sum_of_rating', models.IntegerField()),
                ('average', models.FloatField(null=0.0)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Rating'),
        ),
        migrations.AddField(
            model_name='food',
            name='restaurent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Restaurent'),
        ),
        migrations.AddField(
            model_name='restaurent',
            name='rating',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Rating'),
        ),
    ]
