# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225)),
                ('surname', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=225)),
                ('topic', models.CharField(max_length=225)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
