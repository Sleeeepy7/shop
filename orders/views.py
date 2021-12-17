from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem, Product
from .forms import OrderCreateForm
from cart.views import get_cart, cart_clear
from decimal import Decimal


def order_create(request):
    cart = get_cart(request)
    cart_qty = sum(item['quantity'] for item in cart.values())
    transport_cost = round((3.99 + (cart_qty // 10) * 1.5), 2)

    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            cf = order_form.cleaned_data
            transport = cf['transport']

            if transport == 'Recipient pickup':
                transport_cost = 0

            order = order_form.save(commit=False)
            order.transport_cost = Decimal(transport_cost)
            order.save()

            product_ids = cart.keys()
            products = Product.objects.filter(id__in=product_ids)

            for product in products:
                cart_item = cart[str(product.id)]
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=cart_item['price'],
                    quantity=cart_item['quantity']
                )
            cart_clear(request)
            return render(request, 'order/order_created.html',
                          {'order': order}
                          )
    else:
        order_form = OrderCreateForm()

    return render(request, 'order/order_create.html',
                  {'cart': cart,
                   'order_form': order_form,
                   'transport_cost': transport_cost
                   }
                  )
