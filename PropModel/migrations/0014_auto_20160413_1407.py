# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropModel', '0013_payment_paid_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Paid_To',
            field=models.ForeignKey(to='PropModel.Student'),
        ),
    ]
