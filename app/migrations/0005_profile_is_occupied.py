# Generated by Django 4.0 on 2024-02-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_participant_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_occupied',
            field=models.BooleanField(default=False),
        ),
    ]
