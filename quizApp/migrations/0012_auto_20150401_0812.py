# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0011_auto_20150401_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurations',
            name='count_answers',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(5)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configurations',
            name='count_questions',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(5)]),
            preserve_default=True,
        ),
    ]
