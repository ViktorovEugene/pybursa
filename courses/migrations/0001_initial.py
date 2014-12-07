# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=225)),
                ('course_name', models.CharField(max_length=225)),
                ('instructor', models.CharField(max_length=225)),
                ('assistant', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('date_of_start', models.DateField()),
                ('date_of_end', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
