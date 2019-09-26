from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.http import HttpResponseForbidden

def collection(request, **kwargs):
    context = {}
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    user_pk = kwargs.get('pk')
    if user_pk:
        posts = posts.filter(author_id=user_pk)
        if user_pk == request.user.pk:
            context['is_author'] = True
    context['posts'] = posts
    return render(request, 'blog/collection.html', context)

def post_delete(request, id):
    obj = get_object_or_404(Post, id=id)
    if not request.user.id == obj.author.id:
        return HttpResponseForbidden()

    if request.method == "POST":
        obj.delete()
        return redirect('collection')
    context = {
        "object": obj
    }
    return render(request, 'blog/base.html', context)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('collection')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {"form": form})

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('collection')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {"form": form})


  
