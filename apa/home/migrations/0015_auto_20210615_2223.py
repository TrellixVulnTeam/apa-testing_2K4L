# Generated by Django 3.1.4 on 2021-06-15 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20210615_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 22, 23, 53, 122451)),
        ),
    ]
