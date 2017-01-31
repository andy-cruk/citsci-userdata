# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0012_auto_20151214_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizenopinion',
            name='answer_option',
        ),
        migrations.RemoveField(
            model_name='citizenopinion',
            name='confidence',
        ),
        migrations.RemoveField(
            model_name='citizenopinion',
            name='project',
        ),
        migrations.RemoveField(
            model_name='citizenopinion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='citizenopinion',
            name='user',
        ),
    ]
