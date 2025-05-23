# Generated by Django 4.2.19 on 2025-05-24 23:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wonitApi', '0011_purchase_reference_alter_games_date_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('notification_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'Notifications',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='games',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2025, 5, 24, 23, 1, 3, 43150, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='games',
            name='matchday',
            field=models.DateField(default=datetime.datetime(2025, 5, 24, 23, 1, 3, 43114, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='games',
            name='time_created',
            field=models.TimeField(default=datetime.datetime(2025, 5, 24, 23, 1, 3, 43136, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='slips',
            name='category',
            field=models.CharField(choices=[('free', 'Free'), ('vvip1', 'DAILY VVIP PLAN'), ('vvip2', 'DAILY VVIP PLAN 2'), ('vvip3', 'DAILY VVIP PLAN 3'), ('vip', 'VIP PLAN')], default='', max_length=50),
        ),
    ]
