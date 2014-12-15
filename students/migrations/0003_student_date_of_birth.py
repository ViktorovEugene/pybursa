# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20141214_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
