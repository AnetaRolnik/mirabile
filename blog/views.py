from django.shortcuts import render
from django.utils import timezone
from .models import Post

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