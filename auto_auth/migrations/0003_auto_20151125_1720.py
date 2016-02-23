# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto_auth', '0002_auto_20150320_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='sex',
            field=models.CharField(default=b'\xe4\xba\xba\xe5\xa6\x96', max_length=2, choices=[('\u4eba\u5996', '\u4eba\u5996'), ('\u7537', '\u7537'), ('\u5973', '\u5973')]),
            preserve_default=True,
        ),
    ]
