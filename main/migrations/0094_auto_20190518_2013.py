# Generated by Django 2.2.1 on 2019-05-18 18:13

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0093_auto_20190518_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_image', verbose_name='profile_image')),
                ('user', models.OneToOneField(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 18, 20, 13, 19, 653091), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='datetimeUser',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 18, 20, 13, 19, 654087), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
