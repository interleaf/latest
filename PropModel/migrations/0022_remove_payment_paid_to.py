# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropModel', '0021_auto_20160413_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='Paid_To',
        ),
    ]
