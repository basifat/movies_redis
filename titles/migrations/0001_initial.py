# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('overview', models.TextField(blank=True, null=True)),
                ('new', models.CharField(max_length=30)),
            ],
        ),
    ]
