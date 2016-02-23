# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='realname',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='authuser',
            name='sex',
            field=models.CharField(default=b'\xe4\xba\xba\xe5\xa6\x96', max_length=2, choices=[(b'\xe7\x94\xb7', '\u7537'), ('\u5973', '\u5973'), ('\u4eba\u5996', '\u4eba\u5996')]),
            preserve_default=True,
        ),
    ]
