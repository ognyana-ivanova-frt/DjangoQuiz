# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0009_auto_20150330_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configurations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count_questions', models.IntegerField()),
                ('count_answers', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
