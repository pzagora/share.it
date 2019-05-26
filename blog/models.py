from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    topic_image = models.ImageField(upload_to='profile_image', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self):
        return self.title


class Comments(models.Model):
    user_comments = models.TextField(max_length=250, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_key = models.ForeignKey(Post, related_name='comments', default=1, verbose_name="Post",
                                           on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.user_comments
