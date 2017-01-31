# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0011_citizenopinion_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizenopinion',
            name='confidence',
            field=models.IntegerField(null=True),
        ),
    ]
