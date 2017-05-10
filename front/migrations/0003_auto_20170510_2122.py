# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20170510_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='sexe_court',
            new_name='sexe',
        ),
        migrations.AlterField(
            model_name='animal',
            name='date_publication',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='num_puce',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]