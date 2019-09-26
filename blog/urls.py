from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.collection, name='collection'),
    path('<int:pk>/', views.collection, name='collection'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:id>/delete', views.post_delete, name='post_delete'),
    path('post/<int:id>/edit', views.post_edit, name='post_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
