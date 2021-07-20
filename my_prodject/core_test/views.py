from django.shortcuts import render
from django.http import HttpResponse
from django.urls.conf import path

# Create your views here.


def index(reguest):
    return HttpResponse('Hello World')


def test(reguest):
    return HttpResponse('--ТЕСТВАЯ СТРАНИЦА--')

