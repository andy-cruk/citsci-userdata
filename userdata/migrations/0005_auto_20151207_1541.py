# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0004_citizenopinion'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpinionQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
                ('question_type', models.IntegerField(choices=[(1, b'Text'), (2, b'SingleOptionList'), (3, b'MultiOptionList'), (4, b'YesNo')])),
                ('sequence', models.PositiveSmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpinionQuestionOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100)),
                ('sequence', models.PositiveSmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='citizen',
            options={'ordering': ['short_name']},
        ),
        migrations.AlterModelOptions(
            name='citizenopinion',
            options={'ordering': ['datetime']},
        ),
        migrations.AlterModelOptions(
            name='citsciproject',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='citizenopinion',
            name='project',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
    ]
