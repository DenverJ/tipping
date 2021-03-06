# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_team_fox_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='date',
            new_name='start_time',
        ),
        migrations.RemoveField(
            model_name='game',
            name='id',
        ),
        migrations.AddField(
            model_name='game',
            name='fixture_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='stadium',
            field=models.CharField(default='home', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('O', 'Ongoing'), ('C', 'Completed')], default='P', max_length=10),
        ),
        migrations.AlterField(
            model_name='team',
            name='fox_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
