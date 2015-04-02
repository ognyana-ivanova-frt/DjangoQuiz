# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0017_auto_20150401_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurations',
            name='count_answers',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configurations',
            name='count_questions',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
