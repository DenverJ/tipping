# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_roundscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='special',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
