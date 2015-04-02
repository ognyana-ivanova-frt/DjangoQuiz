# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0006_auto_20150330_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([]),
        ),
    ]
