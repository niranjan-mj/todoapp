# Generated by Django 2.0 on 2019-08-14 12:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_auto_20190705_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 14, 12, 9, 17, 165684, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(),
        ),
    ]
