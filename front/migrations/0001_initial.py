# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 17:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('nom', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=30)),
                ('date_naissance', models.DateField(default=datetime.datetime.today)),
                ('sexe_court', models.CharField(choices=[('F', 'Femelle'), ('M', 'Male')], default='F', max_length=1)),
                ('origine', models.CharField(max_length=200)),
                ('apparence', models.CharField(max_length=200)),
                ('taille', models.CharField(choices=[('S', 'Petit'), ('M', 'Moyen'), ('L', 'Grand'), ('XL', 'Très grand')], default='M', max_length=2)),
                ('temperament', models.CharField(max_length=200)),
                ('num_puce', models.CharField(max_length=100)),
                ('statut', models.CharField(choices=[('01', 'à adopter'), ('02', 'en attente'), ('03', 'adopté'), ('04', 'inactif')], default='01', max_length=2)),
            ],
        ),
    ]
