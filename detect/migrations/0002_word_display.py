# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='display',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
