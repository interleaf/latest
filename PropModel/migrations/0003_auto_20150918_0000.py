# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PropModel', '0002_auto_20150917_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugfixrequest',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proplisting',
            name='property',
            field=models.ForeignKey(default=1, to='PropModel.Property'),
            preserve_default=False,
        ),
    ]
