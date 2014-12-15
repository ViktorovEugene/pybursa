# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tecnology',
            field=models.CharField(max_length=11, choices=[(b'python', b'Python'), (b'rubby', b'Ruby'), (b'javascript', b'JavaScript')]),
            preserve_default=True,
        ),
    ]
