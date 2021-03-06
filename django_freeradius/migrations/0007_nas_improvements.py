# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_freeradius', '0006_postauth_improvements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nas',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='nas',
            name='name',
            field=models.CharField(db_column='nasname', db_index=True, help_text='NAS Name (or IP address)', max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='nas',
            name='ports',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ports'),
        ),
        migrations.AlterField(
            model_name='nas',
            name='server',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='server'),
        ),
        migrations.AlterField(
            model_name='nas',
            name='type',
            field=models.CharField(default='other', max_length=30, verbose_name='type'),
        ),
    ]
