# Generated by Django 2.1.5 on 2019-02-18 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agriculture', '0004_auto_20190218_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agriculturepost',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 16, 21, 44, 918186)),
        ),
    ]