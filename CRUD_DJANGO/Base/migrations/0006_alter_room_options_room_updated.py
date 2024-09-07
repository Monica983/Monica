# Generated by Django 5.1 on 2024-09-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0005_messageitem_conversation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('-updated', '-created')},
        ),
        migrations.AddField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
