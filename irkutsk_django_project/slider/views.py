from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница со слайдером"""
    return render(request, 'slider/index.html')


def my_test_page(request):
    return HttpResponse("Приложение работает!")
