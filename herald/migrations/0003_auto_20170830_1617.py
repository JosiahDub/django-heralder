# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-30 21:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    replaces = [
        (b'herald', '0002_auto_20161017_1201'), (b'herald', '0003_auto_20161021_1448'),
        (b'herald', '0004_notification_verbose_name'), (b'herald', '0005_merge_20170407_1316'),
        (b'herald', '0006_auto_20170825_1813')
    ]

    dependencies = [
        ('auth', '__latest__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('herald', '0002_sentnotification_attachments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_class', models.CharField(max_length=80, unique=True)),
                ('verbose_name', models.CharField(blank=True, max_length=100, null=True)),
                ('can_disable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('disabled_notifications', models.ManyToManyField(to='herald.Notification')),
            ],
        ),
        migrations.AddField(
            model_name='sentnotification',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sentnotification',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Pending'), (1, 'Success'), (2, 'Failed'), (3, 'User Disabled')], default=0),
        ),
    ]
