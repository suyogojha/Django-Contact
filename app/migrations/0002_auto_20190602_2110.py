# Generated by Django 2.2 on 2019-06-03 04:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 2, 21, 10, 25, 399489)),
        ),
    ]
