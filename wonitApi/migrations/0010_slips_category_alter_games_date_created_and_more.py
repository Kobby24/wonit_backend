# Generated by Django 4.2.19 on 2025-05-13 21:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wonitApi', '0009_remove_bookingcode_code_bookingcode_betway_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slips',
            name='category',
            field=models.CharField(choices=[('free', 'Free'), ('paid', 'Vvip')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='games',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2025, 5, 13, 21, 54, 54, 945620, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='games',
            name='matchday',
            field=models.DateField(default=datetime.datetime(2025, 5, 13, 21, 54, 54, 945534, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='games',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2025, 5, 13, 21, 54, 54, 945596, tzinfo=datetime.timezone.utc)),
        ),
    ]
