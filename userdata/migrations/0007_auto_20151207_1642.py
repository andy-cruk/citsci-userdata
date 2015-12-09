# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0006_auto_20151207_1556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opinionquestion',
            options={'ordering': ['sequence']},
        ),
        migrations.AlterModelOptions(
            name='opinionquestionoption',
            options={'ordering': ['sequence']},
        ),
        migrations.AddField(
            model_name='opinionquestion',
            name='options',
            field=models.ManyToManyField(to='userdata.OpinionQuestionOption'),
            preserve_default=True,
        ),

    ]
