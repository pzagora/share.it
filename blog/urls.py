from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from django.conf.urls import url,include
from . import views

app_name = 'main'

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-detail'),
    url(r'^(?P<pk>[-\w]+)/$', views.add_comment, name='add_comment')
]
