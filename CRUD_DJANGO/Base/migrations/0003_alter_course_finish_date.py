# Generated by Django 5.1 on 2024-09-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_alter_module_finish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='finish_date',
            field=models.DurationField(auto_created=True),
        ),
    ]
