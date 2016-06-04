# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='stock_name')),
                ('followers_number', models.PositiveIntegerField(default=0, verbose_name='followers_number')),
                ('new_followers_number', models.IntegerField(default=0, verbose_name='increased_number')),
                ('value_increased_percent', models.CharField(blank=True, max_length=10, null=True, verbose_name='increase_percent')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
            ],
            options={
                'ordering': ['new_followers_number', 'update_time'],
                'verbose_name': '\u80a1\u7968\u4fe1\u606f',
            },
        ),
    ]
