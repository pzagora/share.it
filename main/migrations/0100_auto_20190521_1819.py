# Generated by Django 2.1.7 on 2019-05-21 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0099_auto_20190520_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'user'},
        ),
        migrations.AddField(
            model_name='topiccategory',
            name='slug',
            field=models.SlugField(default=1, max_length=120),
        ),
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 21, 18, 19, 3, 756357), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='datetimeUser',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 21, 18, 19, 3, 757353), verbose_name='date published'),
        ),
    ]
