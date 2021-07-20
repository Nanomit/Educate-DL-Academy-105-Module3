from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import index, test


urlpatterns = [
    url('test/', test, name='test'),
    path('', index, name='index')
]