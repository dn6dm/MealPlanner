# Generated by Django 2.1.2 on 2018-11-13 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0007_auto_20181111_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodplan',
            name='calories',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='carbs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='fat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='protein',
            field=models.IntegerField(default=0),
        ),
    ]
