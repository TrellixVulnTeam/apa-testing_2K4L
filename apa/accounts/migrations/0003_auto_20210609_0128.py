# Generated by Django 3.1.4 on 2021-06-08 19:58

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210609_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, default='static/deafult.png', null=True, upload_to=accounts.models.upload_location),
        ),
    ]
