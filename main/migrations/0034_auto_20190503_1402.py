# Generated by Django 2.1.7 on 2019-05-03 12:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20190503_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_comments', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 14, 2, 13, 789115), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='topicinformation',
            name='comment_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 14, 2, 13, 788116), verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='topicinformation',
            name='topic_category_key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.UserComments', verbose_name='Comments'),
        ),
    ]
