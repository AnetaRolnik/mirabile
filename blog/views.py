from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


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
            messages.success(request, 'Zdjęcie zostało dodane.')
            return redirect(reverse('collection', kwargs={'pk': post.author.id}))
        else:
            messages.error(request, 'Dodawanie zdjęcia nie powiodło się.')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {"form": form})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if not request.user.id == post.author.id:
        return HttpResponseForbidden()

    post.delete()
    messages.success(request, 'Zdjęcie zostało usunięte.')
    return redirect(reverse('collection', kwargs={'pk': post.author.id}))

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
            messages.success(request, 'Zdjęcie zostało edytowane.')
            return redirect(reverse('collection', kwargs={'pk': post.author.id}))
        else:
            messages.error(request, 'Edytowanie zdjęcia nie powiodło się.')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {"form": form})

class ExtendedLoginView(LoginView):
    template_name='blog/registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('collection'))
        return super(LoginView, self).dispatch(request, *args, **kwargs)


def infinite_scroll(request, page, number_of_elem):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(posts, number_of_elem)

    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    context = [{'author':n.author.username, 'photo_url': n.photo.url, 'published_date': n.published_date} for n in list(numbers)]
    return JsonResponse({'collection': context})