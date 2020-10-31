# Generated by Django 3.0.4 on 2020-04-03 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=25)),
                ('material1', models.CharField(max_length=25)),
                ('material2', models.CharField(max_length=25)),
                ('material3', models.CharField(max_length=25)),
            ],
        ),
    ]