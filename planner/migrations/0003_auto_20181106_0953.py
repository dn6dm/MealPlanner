# Generated by Django 2.1.2 on 2018-11-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_fooditem_serving_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='serving_size',
            field=models.CharField(max_length=50),
        ),
    ]
