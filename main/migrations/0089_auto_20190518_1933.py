# Generated by Django 2.2.1 on 2019-05-18 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0088_auto_20190518_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 18, 19, 33, 14, 61973), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='datetimeUser',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 18, 19, 33, 14, 62970), verbose_name='date published'),
        ),
    ]
