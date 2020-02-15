from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.http import HttpResponseForbidden
from django.contrib import messages


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

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if form.cleaned_data.get('manage_post') == 'now':
                post.published_date = timezone.now()
            print(form.cleaned_data)
            post.author = request.user
            post.save()
            messages.success(request, 'Post został dodany.')
            return redirect(reverse('collection', kwargs={'pk': post.author.id}))
    else:
        form = PostForm()
        messages.error(request, 'Dodawanie postu nie powiodło się.')
    return render(request, 'blog/post_new.html', {"form": form})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if not request.user.id == post.author.id:
        return HttpResponseForbidden()

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Zdjęcie zostało usunięte.')
        return redirect(reverse('collection', kwargs={'pk': post.author.id}))
    else:
        messages.error(request, 'Usuwanie zdjęcia nie powiodło się.')
    context = {
        "post": post
    }
    return render(request, 'blog/base.html', context)

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if not request.user.id == post.author.id:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post został edytowany.')
            return redirect(reverse('collection', kwargs={'pk': post.author.id}))
    else:
        form = PostForm(instance=post)
        messages.error(request, 'Edytowanie postu nie powiodło się.')
    return render(request, 'blog/post_new.html', {"form": form})



