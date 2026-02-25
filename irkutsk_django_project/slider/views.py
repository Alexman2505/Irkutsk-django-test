from django.shortcuts import render
from django.http import HttpResponse
from .models import SliderImage


def index(request):
    slides = SliderImage.objects.filter(is_active=True)
    return render(request, 'slider/index.html', {'slides': slides})


# def index(request):
#     """Главная страница со слайдером"""
#     return render(request, 'slider/index.html')


def my_test_page(request):
    return HttpResponse("Приложение работает!")
