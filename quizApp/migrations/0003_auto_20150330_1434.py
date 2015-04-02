# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0002_auto_20150330_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=60)),
                ('correct', models.BooleanField(default=0)),
                ('question', models.ForeignKey(related_name='answers', to='quizApp.Question')),
            ],
            options={
                'ordering': ['question__order'],
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('question',)]),
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['order']},
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(default=1, unique=True, max_length=200),
            preserve_default=False,
        ),
    ]
