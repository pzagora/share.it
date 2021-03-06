# Generated by Django 2.1.7 on 2019-05-02 13:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190502_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 15, 35, 56, 640965), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='topiccategory',
            name='profile',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topicinformation',
            name='comment_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 15, 35, 56, 640007), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='topicinformation',
            name='user_profile',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
