# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('realname', models.CharField(max_length=64, null=True)),
                ('sex', models.CharField(default=b'\xe4\xba\xba\xe5\xa6\x96', max_length=2, choices=[(b'1', '\u7537'), (b'2', '\u5973'), (b'3', b'\xe4\xba\xba\xe5\xa6\x96')])),
                ('api_key', models.CharField(max_length=200, blank=True)),
                ('secretkey', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u8868',
                'verbose_name_plural': '\u7528\u6237\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PermissionList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'URL\u6743\u9650\u8868',
                'verbose_name_plural': 'URL\u6743\u9650\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoleGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('permission', models.ManyToManyField(to='auto_auth.PermissionList', null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u6743\u9650\u7ec4',
                'verbose_name_plural': '\u6743\u9650\u7ec4',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='authuser',
            name='role',
            field=models.ForeignKey(blank=True, to='auto_auth.RoleGroup', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
