# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-11 08:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_location'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
    ]