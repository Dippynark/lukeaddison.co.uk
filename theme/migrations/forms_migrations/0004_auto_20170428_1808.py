# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_form_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='background',
        ),
        migrations.RemoveField(
            model_name='form',
            name='subtitle',
        ),
    ]
