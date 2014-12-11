# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225)),
                ('surname', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15, blank=True)),
                ('package', models.CharField(default=b's', max_length=1, choices=[(b's', b'Standart'), (b'g', b'Glod'), (b'p', b'Platinum')])),
                ('courses', models.ManyToManyField(to='courses.Course', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
