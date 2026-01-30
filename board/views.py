from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Post
from .forms import PostForm, CommentForm

def index(request):
    # Sort by number of comments (descending) first, then by creation time (newest first)
    posts = Post.objects.annotate(num_comments=Count('comments')).order_by('-num_comments', '-created_at')
    
    post_form = PostForm()
    comment_form = CommentForm()
    
    return render(request, 'board/index.html', {
        'posts': posts,
        'post_form': post_form,
        'comment_form': comment_form
    })

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # Check if user is logged in and is staff/superuser
            if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
                post.is_admin = True
            post.save()
    return redirect('index')

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            # Check if user is logged in and is staff/superuser
            if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
                comment.is_admin = True
            comment.save()
    return redirect('index')
