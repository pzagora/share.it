from django.db import models
from datetime import datetime
# Create your models here.


class TopicCategory(models.Model):
    topic_category = models.CharField(max_length=30)
    topic_title = models.CharField(max_length=200)
    topic_image = models.ImageField()
    datetime = models.DateTimeField("date published", default=datetime.now())

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.topic_category


class TopicInformation(models.Model):
    topic_summary = models.CharField(max_length=200)
    topic_comments = models.CharField(max_length=200)
    comment_published: datetime = models.DateTimeField("date published", default=datetime.now())
    topic_category_key = models.ForeignKey(TopicCategory, default=1, verbose_name="Categories", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.topic_summary
