from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'frontend/index.html', {'products': products})


def expenses(request):
    return render(request, 'frontend/expenses.html')


def vote(request):
    return render(request, 'frontend/vote.html')
