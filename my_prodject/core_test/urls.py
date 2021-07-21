from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('users/<int:user_id>/', views.user, name='user'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/create/',views.post_create, name='post_create'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('post/', views.post_all, name='post_all'),
]