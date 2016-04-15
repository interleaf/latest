# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropModel', '0017_payment_paid_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Paid_To',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Paid to', blank=True),
        ),
    ]
