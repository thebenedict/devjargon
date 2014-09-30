# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detect', '0003_remove_document_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
    ]
