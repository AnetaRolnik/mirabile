from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.collection, name='collection'),
    path('<int:pk>/', views.collection, name='collection'),
    path('<int:pk>/post/<int:id>/delete', views.post_delete, name='post_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
