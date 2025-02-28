# Generated by Django 5.1.4 on 2025-02-21 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_category_question_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='QuestionCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.question')),
            ],
        ),
    ]
