# Generated by Django 2.1.7 on 2019-05-02 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190502_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 15, 36, 57, 887469), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='topicinformation',
            name='comment_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 15, 36, 57, 886473), verbose_name='date published'),
        ),
    ]