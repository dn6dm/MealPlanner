# Generated by Django 2.1.2 on 2018-11-02 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_profile_calories'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('calories', models.IntegerField(default=0)),
                ('carbs', models.IntegerField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('protein', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FoodPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.IntegerField(default=0)),
                ('carbs', models.IntegerField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('protein', models.IntegerField(default=0)),
                ('fooditems', models.ManyToManyField(to='planner.FoodItem')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
    ]
