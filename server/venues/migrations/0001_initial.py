# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=300)),
                ('timings', models.CharField(max_length=200)),
                ('contactno', models.CharField(max_length=200)),
                ('venue_create_time', models.DateTimeField(verbose_name='Time Created', auto_now_add=True)),
                ('venue_update_time', models.DateTimeField(verbose_name='Time Modified', auto_now=True)),
                ('sports', models.ManyToManyField(to='sports.Sport')),
            ],
        ),
    ]
