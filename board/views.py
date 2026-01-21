from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm

def index(request):
    posts = Post.objects.all()
    post_form = PostForm()
    comment_form = CommentForm()
    
    return render(request, 'board/index.html', {
        'posts': posts,
        'post_form': post_form,
        'comment_form': comment_form
    })

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('index')

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('index')
