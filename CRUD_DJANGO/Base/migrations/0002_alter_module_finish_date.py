# Generated by Django 5.1 on 2024-09-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='finish_date',
            field=models.DurationField(auto_created=True),
        ),
    ]
