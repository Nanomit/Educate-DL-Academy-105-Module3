from django.shortcuts import render
from django.http import HttpResponse
from django.urls.conf import path
from django.db.models import Sum

from .models import Posting

# Create your views here.


def index(reguest):
    #posts = Posting.objects.filter(category = post).order_by('-date_added')[:5]
    return HttpResponse('---Главная страница---')


def post(reguest, post_id):
    return HttpResponse('---Страница объявления---')


def user(reguest, user_id):
    return HttpResponse('---Страница пользователя---')


def post_edit(request, post_id):
    return HttpResponse('---Редактирование объявления---')


def post_create(request):
    return HttpResponse('---Создание объявления---')


def post_delete(request, post_id):
    return HttpResponse('---Удаление объявления---')


def post_all(request):
    return HttpResponse('---Популярные объявления---')


