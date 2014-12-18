# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_dossier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='courses',
            field=models.ManyToManyField(related_name='dossier_courses', to='courses.Course', blank=True),
            preserve_default=True,
        ),
    ]
