# Generated by Django 2.1.7 on 2019-05-03 17:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20190503_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccategory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 19, 33, 33, 840820), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usercomments',
            name='comment_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 19, 33, 33, 841818), verbose_name='date published'),
        ),
        migrations.RemoveField(
            model_name='usercomments',
            name='topic_category_key',
        ),
        migrations.AddField(
            model_name='usercomments',
            name='topic_category_key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='comments', to='main.TopicCategory', verbose_name='Categories'),
        ),
    ]
