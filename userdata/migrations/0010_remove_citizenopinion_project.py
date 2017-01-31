# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0009_auto_20151211_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizenopinion',
            name='project',
        ),
    ]
