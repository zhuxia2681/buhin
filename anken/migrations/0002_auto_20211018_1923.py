# Generated by Django 3.2.8 on 2021-10-18 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anken', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anken',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 18, 19, 23, 21, 185471), verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='anken',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 18, 19, 23, 21, 185486), verbose_name='更新日時'),
        ),
    ]
