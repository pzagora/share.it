# Generated by Django 2.1.7 on 2019-05-02 13:20

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190502_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default=1, max_length=20, verbose_name=django.contrib.auth.models.User)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.RemoveField(
            model_name='topicinformation',
            name='user',
        ),
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 15, 20, 48, 68794), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='topicinformation',
            name='comment_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 15, 20, 48, 67797), verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='topiccategory',
            name='profile_key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Profile', verbose_name='Profiles'),
        ),
    ]