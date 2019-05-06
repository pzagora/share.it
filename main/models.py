from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class TopicInformation(models.Model):
    topic_summary = models.CharField(max_length=200)
    topic_comments = models.CharField(max_length=200)
    comment_published: datetime = models.DateTimeField("date published", default=datetime.now())

    class Meta:
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.topic_summary


class TopicCategory(models.Model):
    topic_category = models.CharField(max_length=30)
    topic_title = models.CharField(max_length=200)
    topic_image = models.ImageField(upload_to='profile_image', blank=True)
    datetime = models.DateTimeField("date published", default=datetime.now())
    topic_category_key = models.ForeignKey(TopicInformation, default=1, verbose_name="Topics", on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.topic_category
