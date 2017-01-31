# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0015_citizenopinion_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizenopinion',
            name='answer_option',
            field=models.ForeignKey(to='userdata.OpinionQuestionOption', null=True),
            preserve_default=True,
        ),
    ]
