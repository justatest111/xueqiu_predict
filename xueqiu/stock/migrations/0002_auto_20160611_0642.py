# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-11 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['-new_followers_number', 'update_time'], 'verbose_name': '\u80a1\u7968\u4fe1\u606f'},
        ),
    ]
