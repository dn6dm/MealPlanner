# Generated by Django 2.1.2 on 2018-11-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0008_auto_20181113_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodplan',
            name='name',
            field=models.CharField(default='Apple', max_length=50),
            preserve_default=False,
        ),
    ]