# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0020_auto_20150401_0837'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Configurations',
        ),
    ]
