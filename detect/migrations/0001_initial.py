# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('total_word_count', models.PositiveIntegerField()),
                ('source_file', models.FileField(upload_to=b'documents')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='document',
            name='organization',
            field=models.ForeignKey(to='detect.Organization'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stem', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WordCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='document',
            name='word_counts',
            field=models.ManyToManyField(to='detect.Word', through='detect.WordCount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wordcount',
            name='document',
            field=models.ForeignKey(to='detect.Document'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wordcount',
            name='word',
            field=models.ForeignKey(to='detect.Word'),
            preserve_default=True,
        ),
    ]
