# Generated by Django 4.2.19 on 2025-05-25 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wonitApi', '0013_notifications_cleared_notifications_seen_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='message',
            new_name='body',
        ),
        migrations.AddField(
            model_name='notifications',
            name='title',
            field=models.TextField(default='f'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='games',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2025, 5, 24, 23, 57, 47, 361174, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='games',
            name='matchday',
            field=models.DateField(default=datetime.datetime(2025, 5, 24, 23, 57, 47, 361138, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='games',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2025, 5, 24, 23, 57, 47, 361164, tzinfo=datetime.timezone.utc)),
        ),
    ]
