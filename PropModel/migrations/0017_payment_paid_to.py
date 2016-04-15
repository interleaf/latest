# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropModel', '0016_remove_payment_paid_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='Paid_To',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
