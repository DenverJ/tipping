# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 09:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_auto_20160212_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoundScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Round')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
