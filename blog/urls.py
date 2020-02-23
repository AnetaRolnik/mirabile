from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.collection, name='collection'),
    path('<int:pk>/', views.collection, name='collection'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:id>/delete', views.post_delete, name='post_delete'),
    path('post/<int:id>/edit', views.post_edit, name='post_edit'),
    path('login/', views.ExtendedLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/base.html'), name='logout'),
    path('<int:page>/<int:number_of_elem>', views.infinite_scroll, name='infinite_scroll')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
