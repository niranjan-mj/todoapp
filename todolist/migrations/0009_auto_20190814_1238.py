# Generated by Django 2.0 on 2019-08-14 12:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0008_auto_20190814_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 14, 12, 38, 26, 23326, tzinfo=utc)),
        ),
    ]