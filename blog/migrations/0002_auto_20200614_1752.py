# Generated by Django 3.0.7 on 2020-06-14 14:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2020, 6, 14, 14, 52, 7, 276625, tzinfo=utc)),
        ),
    ]
