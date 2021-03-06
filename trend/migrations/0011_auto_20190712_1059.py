# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-12 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0010_auto_20190711_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('Menswear', 'Menswear'), ('womenswear', 'womenswear'), ('Generalised', 'Generalised')], default='menswear', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Rocker looks', 'Rocker looks'), ('Tomboy Fashion', 'Tomboy Fashion'), ('Sophisticated Fashion', 'Sophisticated Fashion'), ('Artsy Fashion', 'Artsy Fashion'), ('Casual Fashion', 'Casual Fashion'), ('Vintage Fashion', 'Vintage Fashion')], default='No style', max_length=100),
        ),
    ]
