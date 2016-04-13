# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropModel', '0009_auto_20160411_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='Pay_By',
            new_name='Notes',
        ),
        migrations.AddField(
            model_name='payment',
            name='Paid_By',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='City',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Notes',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='State',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Zip',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
