from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comments
from django.views.generic import ListView, DetailView, CreateView
from users.forms import CommentForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Comments
    fields = [' user_comments',]


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('main:blog-home', pk = post.id)
    else:
        form = CommentForm()
    template = 'blog/add_comment.html'
    context = {'form':form}
    return render(request, template, context)













