# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='slug',
        ),
    ]
