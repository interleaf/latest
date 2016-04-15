# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropModel', '0024_volunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='Phone_Number',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
