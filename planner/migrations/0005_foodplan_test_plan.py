# Generated by Django 2.1.2 on 2018-11-06 20:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_auto_20181106_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodplan',
            name='test_plan',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), default=list, size=None),
        ),
    ]
