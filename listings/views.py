from django.shortcuts import render
from .models import *


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'product/list.html',
                  {'categories': categories, 'products': products})
