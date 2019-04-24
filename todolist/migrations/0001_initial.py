# Generated by Django 2.1.3 on 2019-04-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateField(default='2019-04-24')),
                ('due_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
