# Generated by Django 2.1.7 on 2019-05-07 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0057_auto_20190507_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 7, 15, 29, 10, 171242), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='datetimeUser',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 7, 15, 29, 10, 171242), verbose_name='date published'),
        ),
    ]