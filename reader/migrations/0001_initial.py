# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-26 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emaildata',
            fields=[
                ('eid', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('emailid', models.EmailField(max_length=255)),
                ('rdatetime', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
    ]
