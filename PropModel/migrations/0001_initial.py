# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_date', models.DateField()),
                ('comment_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('revise_date', models.DateField(verbose_name=b'date revised')),
                ('status', models.CharField(max_length=200, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=20, null=True, blank=True)),
                ('state', models.CharField(max_length=2, null=True, blank=True)),
                ('zip', models.CharField(max_length=5, null=True, blank=True)),
                ('asking_price', models.DecimalField(null=True, max_digits=19, decimal_places=2, blank=True)),
                ('prop_size', models.IntegerField(null=True, blank=True)),
                ('prop_size_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('prop_type', models.CharField(max_length=20, null=True, blank=True)),
                ('prop_sub_type', models.CharField(max_length=100, null=True, blank=True)),
                ('year_built', models.IntegerField(null=True, blank=True)),
                ('year_renov', models.IntegerField(null=True, blank=True)),
                ('lot_size', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('lot_size_unit', models.CharField(max_length=5, null=True, blank=True)),
                ('listing_id', models.CharField(max_length=100, null=True, blank=True)),
                ('income_gross', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('expense', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('noi', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('listing_broker', models.CharField(max_length=100, null=True, blank=True)),
                ('broker_number', models.CharField(max_length=50, null=True, blank=True)),
                ('broker_email', models.EmailField(max_length=254, null=True, blank=True)),
                ('occ', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_name', models.CharField(max_length=30)),
                ('model_text', models.TextField()),
                ('create_date', models.DateField(verbose_name=b'date created')),
                ('property', models.ForeignKey(to='PropModel.Property', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='property',
            field=models.ForeignKey(to='PropModel.Property'),
        ),
    ]
