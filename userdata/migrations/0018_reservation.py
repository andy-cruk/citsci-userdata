# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0017_citizenopinion_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventName', models.CharField(max_length=100)),
                ('eventStartDate', models.DateField()),
                ('eventEndDate', models.DateField()),
                ('numberOfDevices', models.PositiveSmallIntegerField()),
                ('deliveryMethod', models.IntegerField(choices=[(1, b'Collect'), (2, b'Post')])),
                ('outDate', models.DateField()),
                ('returnDate', models.DateField()),
                ('bookerName', models.CharField(max_length=255)),
                ('bookerEmail', models.CharField(max_length=255)),
                ('deliveryAddress', models.CharField(default=b'', max_length=255, null=True)),
                ('costCode', models.CharField(default=b'', max_length=10, null=True)),
            ],
            options={
                'ordering': ['outDate'],
            },
            bases=(models.Model,),
        ),
    ]
