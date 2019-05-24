from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=True)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)


class TopicCategory(models.Model):
    topic_summary = models.CharField(max_length=200)
    topic_comment = models.CharField(max_length=200)
    topic_category = models.CharField(max_length=30)
    topic_title = models.CharField(max_length=200)
    topic_image = models.ImageField(upload_to='profile_image', blank=True)
    datetime = models.DateTimeField("date published", default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.topic_category


class UserComments(models.Model):
    user_comments = models.TextField(max_length=250)
    datetimeUser = models.DateTimeField("date published", default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_category_key = models.ForeignKey(TopicCategory, related_name='comments', default=1, verbose_name="Categories",
                                           on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.user_comments


