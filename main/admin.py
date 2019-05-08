from django.contrib import admin
from .models import TopicCategory, UserComments, UserProfile

# Register your models here.
admin.site.register(TopicCategory)
admin.site.register(UserComments)
admin.site.register(UserProfile)