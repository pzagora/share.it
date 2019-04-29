from django.contrib import admin
from .models import TopicInformation, TopicCategory

# Register your models here.
admin.site.register(TopicInformation)
admin.site.register(TopicCategory)