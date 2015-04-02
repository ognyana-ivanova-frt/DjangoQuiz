# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0007_auto_20150330_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=1),
            preserve_default=True,
        ),
    ]
