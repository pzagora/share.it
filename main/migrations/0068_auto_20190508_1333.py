# Generated by Django 2.1.7 on 2019-05-08 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0067_auto_20190508_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 13, 33, 14, 737949), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='datetimeUser',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 13, 33, 14, 737949), verbose_name='date published'),
        ),
    ]
