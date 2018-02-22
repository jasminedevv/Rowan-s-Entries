# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 02:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('relations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Tag'),
        ),
    ]
