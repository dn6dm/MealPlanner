# Generated by Django 2.1.2 on 2018-11-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181101_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='calories',
            field=models.IntegerField(default=2000),
        ),
    ]
