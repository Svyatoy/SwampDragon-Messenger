# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('confs', '0003_auto_20160608_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 4, 16, 28, 409380)),
        ),
        migrations.AlterField(
            model_name='conference',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 2, 4, 16, 28, 409251)),
        ),
    ]
