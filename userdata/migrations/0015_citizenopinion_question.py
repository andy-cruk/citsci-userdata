# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0014_citizenopinion_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizenopinion',
            name='question',
            field=models.ForeignKey(to='userdata.OpinionQuestion', null=True),
            preserve_default=True,
        ),
    ]
