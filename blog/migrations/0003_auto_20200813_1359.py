# Generated by Django 3.0.3 on 2020-08-13 08:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200813_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 8, 29, 19, 98497, tzinfo=utc)),
        ),
    ]
