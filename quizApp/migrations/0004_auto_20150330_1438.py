# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0003_auto_20150330_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.RenameField(
            model_name='question',
            old_name='answer',
            new_name='correct_answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='order',
        ),
    ]
