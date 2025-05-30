# Generated by Django 4.2.19 on 2025-05-11 21:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wonitApi', '0007_add_slip_games_m2m'),
    ]

    operations = [
        migrations.AddField(
            model_name='slips',
            name='booking_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='wonitApi.bookingcode'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='games',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2025, 5, 11, 21, 31, 30, 236676, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='games',
            name='matchday',
            field=models.DateField(default=datetime.datetime(2025, 5, 11, 21, 31, 30, 236603, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='games',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2025, 5, 11, 21, 31, 30, 236651, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='slips',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
    ]
