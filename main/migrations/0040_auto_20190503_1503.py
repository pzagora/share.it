# Generated by Django 2.1.7 on 2019-05-03 13:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_auto_20190503_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicinformation',
            name='topic_category_key',
        ),
        migrations.RemoveField(
            model_name='usercomments',
            name='topic_inf_key',
        ),
        migrations.AddField(
            model_name='topiccategory',
            name='topic_comment',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topiccategory',
            name='topic_summary',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercomments',
            name='topic_category_key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TopicCategory', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 15, 3, 10, 194460), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='comment_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 15, 3, 10, 195457), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='TopicInformation',
        ),
    ]