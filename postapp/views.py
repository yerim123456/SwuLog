from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import PostForm
from .models import Post, Photo, Like
from django.contrib import messages


# @login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for file in request.FILES.getlist('photos'):
                Photo.objects.create(post=post, image=file)
            return redirect(reverse('postapp:post_detail', kwargs={'post_id': post.id}))
    else:
        form = PostForm()
    return render(request, 'postapp/post_create.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    is_liked = False
    if request.user.is_authenticated:
        is_liked = Like.objects.filter(post=post, user=request.user).exists()
    return render(request, 'postapp/post_detail.html', {'post': post, 'is_liked': is_liked})


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'postapp/post_list.html', {'posts': posts})


@login_required
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, "작성자만 수정할 수 있습니다.")
        return redirect('postapp:post_detail', post_id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            if request.FILES.getlist('photos'):
                post.photos.all().delete()
                for file in request.FILES.getlist('photos'):
                    Photo.objects.create(post=post, image=file)

            return redirect('postapp:post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'postapp/post_update.html', {'form': form, 'post': post})


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, "작성자만 삭제할 수 있습니다.")
        return redirect('postapp:post_detail', post_id=post_id)

    post.delete()
    messages.add_message(request, messages.SUCCESS, "게시물이 삭제되었습니다.")
    return redirect('postapp:post_list')


@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect('postapp:post_detail', post_id=post.id)
