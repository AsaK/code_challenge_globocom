# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 23:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participant', '0001_initial'),
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_date', models.DateTimeField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participant.Participant')),
            ],
        ),
    ]