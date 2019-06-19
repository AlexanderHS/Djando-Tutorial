from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
'''
This is a view.
'''


def post_list(request):
    """Return all published posts."""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """Return a specific post only."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
