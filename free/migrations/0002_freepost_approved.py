# Generated by Django 2.1.5 on 2019-02-18 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='freepost',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
