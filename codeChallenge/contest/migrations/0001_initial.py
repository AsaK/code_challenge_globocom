# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='Nome da votação')),
                ('desc', models.TextField(max_length=255, verbose_name='Descrição da votação')),
                ('start_date', models.DateTimeField(verbose_name='Data inicial')),
                ('end_date', models.DateTimeField(verbose_name='Data final')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='Logos', verbose_name='Logo da votação')),
            ],
        ),
    ]
