# Generated by Django 2.1.7 on 2019-05-02 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20190502_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 20, 15, 2, 304616), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='topicinformation',
            name='comment_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 20, 15, 2, 303579), verbose_name='date published'),
        ),
    ]
