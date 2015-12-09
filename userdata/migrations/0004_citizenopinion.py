# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_citizen'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitizenOpinion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('confidence', models.IntegerField()),
                ('user', models.ForeignKey(to='userdata.Citizen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
