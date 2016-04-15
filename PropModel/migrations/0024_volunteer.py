# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropModel', '0023_payment_paid_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_Name', models.CharField(max_length=50, null=True, blank=True)),
                ('Last_Name', models.CharField(max_length=50, null=True, blank=True)),
                ('Phone_Number', models.IntegerField(null=True, blank=True)),
                ('Address', models.CharField(max_length=200, null=True, blank=True)),
                ('City', models.CharField(max_length=20, null=True, blank=True)),
                ('State', models.CharField(max_length=10, null=True, blank=True)),
                ('Zip', models.IntegerField(null=True, blank=True)),
                ('Email', models.CharField(max_length=50, null=True, blank=True)),
                ('Company', models.CharField(max_length=50, null=True, blank=True)),
                ('gender', models.ForeignKey(to='PropModel.Gender')),
            ],
        ),
    ]
