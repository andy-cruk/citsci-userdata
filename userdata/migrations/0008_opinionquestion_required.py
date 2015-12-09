# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0007_auto_20151207_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinionquestion',
            name='required',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
