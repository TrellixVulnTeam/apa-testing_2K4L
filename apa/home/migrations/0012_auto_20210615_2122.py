# Generated by Django 3.1.4 on 2021-06-15 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210615_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 21, 22, 1, 925446)),
        ),
    ]
