from django.db import models
# Create your models here.


class Categories(models.Model):
    sub_title = models.CharField(max_length=200)
    sub_content = models.TextField()
    sub_published = models.DateTimeField('date published')

    def __str__(self):
        return self.sub_title
