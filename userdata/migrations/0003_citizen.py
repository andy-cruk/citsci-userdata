# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_citsciproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=20)),
                ('projects', models.ManyToManyField(to='userdata.CitSciProject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
