# Generated by Django 3.0.7 on 2020-06-15 19:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200615_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2020, 6, 15, 19, 9, 9, 793082, tzinfo=utc)),
        ),
    ]
