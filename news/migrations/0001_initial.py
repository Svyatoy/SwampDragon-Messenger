# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 23:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(default='Lorem ipsum dolor sit amet...', max_length=1000)),
                ('ts_created', models.DateTimeField(auto_now_add=True)),
                ('ts_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_written', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-ts_created'],
                'verbose_name_plural': 'News',
            },
        ),
    ]
