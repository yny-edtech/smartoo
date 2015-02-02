# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_auto_20150201_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisescreator',
            name='parameters',
            field=common.fields.DictField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exercisesgrader',
            name='parameters',
            field=common.fields.DictField(),
            preserve_default=True,
        ),
    ]