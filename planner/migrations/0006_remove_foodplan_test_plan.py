# Generated by Django 2.1.2 on 2018-11-06 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_foodplan_test_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodplan',
            name='test_plan',
        ),
    ]
