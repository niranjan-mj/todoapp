# Generated by Django 2.1.3 on 2019-04-17 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20190417_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
