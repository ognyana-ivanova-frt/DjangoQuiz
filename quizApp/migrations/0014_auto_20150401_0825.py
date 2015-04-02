# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0013_auto_20150401_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurations',
            name='count_answers',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(2)]),
            preserve_default=True,
        ),
    ]
