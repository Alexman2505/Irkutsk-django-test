from django.urls import path
from . import views

urlpatterns = [
    path('my_test_page/', views.my_test_page, name='my_test_page'),
    path('', views.index, name='index'),  # Пустая строка = главная страница
]
