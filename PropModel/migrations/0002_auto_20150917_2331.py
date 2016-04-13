# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PropModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_by', models.CharField(max_length=100)),
                ('comment_date', models.DateField(auto_now_add=True)),
                ('comment_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BugFixRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('request_by', models.CharField(max_length=100)),
                ('request_date', models.DateField(auto_now_add=True, verbose_name=b'Request Date')),
            ],
        ),
        migrations.CreateModel(
            name='BugFixStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bugstatus', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PropComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_date', models.DateField(auto_now_add=True)),
                ('comment_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PropFin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('end_date', models.DateField(auto_now_add=True)),
                ('income_gross', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('expense', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('noi', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('occ', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropListing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listing_id', models.CharField(max_length=100, null=True, blank=True)),
                ('listing_site', models.CharField(max_length=100, null=True, blank=True)),
                ('asking_price', models.DecimalField(null=True, max_digits=19, decimal_places=2, blank=True)),
                ('listing_broker', models.CharField(max_length=100, null=True, blank=True)),
                ('broker_number', models.CharField(max_length=50, null=True, blank=True)),
                ('broker_email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('propstatus', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PropType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prop_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RentRoll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('end_date', models.DateField(auto_now_add=True)),
                ('sub_unit_name', models.TextField()),
                ('rent_collected', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='TimeFreq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timefreq', models.CharField(max_length=20)),
                ('num_month', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('closing_date', models.DateField(auto_now_add=True)),
                ('purchase_price', models.DecimalField(max_digits=12, decimal_places=2)),
                ('closing_cost', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='property',
        ),
        migrations.RemoveField(
            model_name='property',
            name='asking_price',
        ),
        migrations.RemoveField(
            model_name='property',
            name='broker_email',
        ),
        migrations.RemoveField(
            model_name='property',
            name='broker_number',
        ),
        migrations.RemoveField(
            model_name='property',
            name='expense',
        ),
        migrations.RemoveField(
            model_name='property',
            name='income_gross',
        ),
        migrations.RemoveField(
            model_name='property',
            name='listing_broker',
        ),
        migrations.RemoveField(
            model_name='property',
            name='listing_id',
        ),
        migrations.RemoveField(
            model_name='property',
            name='noi',
        ),
        migrations.RemoveField(
            model_name='property',
            name='occ',
        ),
        migrations.RemoveField(
            model_name='property',
            name='prop_type',
        ),
        migrations.AlterField(
            model_name='property',
            name='revise_date',
            field=models.DateField(auto_now_add=True, verbose_name=b'date revised'),
        ),
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.ForeignKey(default=1, to='PropModel.PropStatus'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='transaction',
            name='property',
            field=models.ForeignKey(to='PropModel.Property'),
        ),
        migrations.AddField(
            model_name='rentroll',
            name='freq',
            field=models.ForeignKey(to='PropModel.TimeFreq'),
        ),
        migrations.AddField(
            model_name='rentroll',
            name='property',
            field=models.ForeignKey(to='PropModel.Property'),
        ),
        migrations.AddField(
            model_name='propfin',
            name='freq',
            field=models.ForeignKey(to='PropModel.TimeFreq'),
        ),
        migrations.AddField(
            model_name='propfin',
            name='property',
            field=models.ForeignKey(to='PropModel.Property'),
        ),
        migrations.AddField(
            model_name='propcomment',
            name='property',
            field=models.ForeignKey(to='PropModel.Property'),
        ),
        migrations.AddField(
            model_name='bugfixrequest',
            name='status',
            field=models.ForeignKey(to='PropModel.BugFixStatus'),
        ),
        migrations.AddField(
            model_name='bugcomment',
            name='bug',
            field=models.ForeignKey(to='PropModel.BugFixRequest'),
        ),
        migrations.AddField(
            model_name='property',
            name='proptype',
            field=models.ForeignKey(default=1, to='PropModel.PropType'),
            preserve_default=False,
        ),
    ]
