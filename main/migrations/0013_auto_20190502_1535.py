# Generated by Django 2.1.7 on 2019-05-02 13:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_auto_20190502_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topiccategory',
            name='profile_key',
        ),
        migrations.AddField(
            model_name='topiccategory',
            name='profile',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topicinformation',
            name='user_profile',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 15, 35, 14, 653703), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='topicinformation',
            name='comment_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 15, 35, 14, 652705), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
