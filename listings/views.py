from django.shortcuts import render, get_object_or_404
from .models import *


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    requested_category = None
    products = Product.objects.all()

    if category_slug:
        requested_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=requested_category)

    return render(request, 'product/list.html', {
        'categories': categories,
        'requested_category': requested_category,
        'products': products
    }
                  )
