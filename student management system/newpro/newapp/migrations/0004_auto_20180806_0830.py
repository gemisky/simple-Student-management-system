# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-06 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_student_feestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bus_fee',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='hostel_fee',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='mess_fee',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='tuition_fee',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
