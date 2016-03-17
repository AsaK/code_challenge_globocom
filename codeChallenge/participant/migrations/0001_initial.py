# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, verbose_name='Nome')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Descrição de votação')),
                ('picture', models.ImageField(upload_to='Pictures', verbose_name='Foto')),
                ('active', models.BooleanField(verbose_name='Eliminado')),
                ('contest', models.ManyToManyField(to='contest.Contest', verbose_name='Paredão')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]