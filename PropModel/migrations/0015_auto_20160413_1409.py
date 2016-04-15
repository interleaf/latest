# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropModel', '0014_auto_20160413_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Paid_To',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
