# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0008_opinionquestion_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizenopinion',
            name='answer_option',
            field=models.ForeignKey(to='userdata.OpinionQuestionOption', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='citizenopinion',
            name='answer_text',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='citizenopinion',
            name='question',
            field=models.ForeignKey(to='userdata.OpinionQuestion', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opinionquestion',
            name='options',
            field=models.ManyToManyField(to=b'userdata.OpinionQuestionOption', null=True),
        ),
    ]
