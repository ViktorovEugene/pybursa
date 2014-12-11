# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_index', models.CharField(max_length=60)),
                ('coutry', models.CharField(max_length=60)),
                ('region', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('house', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
