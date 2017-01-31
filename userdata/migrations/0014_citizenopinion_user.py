# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0013_auto_20151214_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizenopinion',
            name='user',
            field=models.ForeignKey(to='userdata.Citizen', null=True),
            preserve_default=True,
        ),
    ]
