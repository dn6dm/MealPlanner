# Generated by Django 2.1.2 on 2018-11-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='serving_size',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
