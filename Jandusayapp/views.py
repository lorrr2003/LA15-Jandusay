from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse

# Define the home view to display all posts
def home(request):
    posts = Post.objects.all()  # Get all posts from the database
    return render(request, 'home.html', {'posts': posts})

# Define the post_detail view to show individual post details
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)  # Fetch post based on the slug
    return render(request, 'post_detail.html', {'post': post})

