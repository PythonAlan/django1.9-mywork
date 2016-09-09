# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-09 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.IntegerField(verbose_name='编号')),
                ('Title', models.CharField(max_length=200, verbose_name='标题')),
                ('Target', models.CharField(max_length=100, verbose_name='目的')),
                ('Steps', models.TextField(max_length=1024, verbose_name='方案')),
                ('Ordered', models.BooleanField(default=False)),
                ('Finisher', models.CharField(max_length=50, verbose_name='负责人')),
                ('Startime', models.DateField(blank=True, null=True, verbose_name='开始时间')),
                ('Endtime', models.DateField(blank=True, null=True, verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '工作流',
                'verbose_name_plural': '工作流',
            },
        ),
        migrations.CreateModel(
            name='Worktype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, verbose_name='工作分类')),
            ],
            options={
                'verbose_name': '工作分类',
                'verbose_name_plural': '工作分类',
            },
        ),
        migrations.AddField(
            model_name='work',
            name='Work_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflow.Worktype'),
        ),
    ]
