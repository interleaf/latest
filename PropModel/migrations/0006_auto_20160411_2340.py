# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 23:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PropModel', '0005_auto_20160411_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='Pay_By',
            new_name='Paid_By',
        ),
    ]
