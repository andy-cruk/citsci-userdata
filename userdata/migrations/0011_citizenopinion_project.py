# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0010_remove_citizenopinion_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizenopinion',
            name='project',
            field=models.ForeignKey(to='userdata.CitSciProject', null=True),
            preserve_default=True,
        ),
    ]
