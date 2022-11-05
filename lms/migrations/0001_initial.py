# Generated by Django 3.2.16 on 2022-11-05 12:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2022, 11, 5, 12, 16, 34, 109974, tzinfo=utc))),
            ],
        ),
    ]