# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-10 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0006_auto_20190710_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[(1, 'Menswear'), (2, 'womenswear'), (3, 'Generalised')], max_length=50),
        ),
    ]
