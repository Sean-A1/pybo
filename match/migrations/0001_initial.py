# Generated by Django 5.1.4 on 2025-03-06 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('date', models.IntegerField()),
                ('day', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('stadium', models.CharField(max_length=20)),
                ('team1', models.CharField(max_length=20)),
                ('team2', models.CharField(max_length=20)),
            ],
        ),
    ]
