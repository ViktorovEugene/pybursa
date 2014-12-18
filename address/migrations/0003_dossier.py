# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20141217_2125'),
        ('address', '0002_auto_20141211_0510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(default=b'red', max_length=6, choices=[(b'red', b'red'), (b'orange', b'orange'), (b'yellow', b'yellow'), (b'green', b'green'), (b'azure', b'azure'), (b'blue', b'blue'), (b'violet', b'violet')])),
                ('address', models.ForeignKey(related_name='dissier_address', blank=True, to='address.Address')),
                ('courses', models.ManyToManyField(to='courses.Course', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
