# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0005_auto_20151207_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citsciproject',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
