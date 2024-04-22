from django.shortcuts import render
from .models import RealtyObjects


def home(request):
    items = RealtyObjects.objects.all()
    data = {
        'items': items,
        'title': 'Главная страница'
    }
    return render(request, 'realty/home.html', data)


def contacts(request):
    return render(request, 'realty/contacts.html', {'title': 'Недвижка'})
