from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello world')


def new_product(request):
    return HttpResponse('Aditi is stupid')
