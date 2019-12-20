from django.shortcuts import render
from rest_framework import generics
from django.core.mail import send_mail

from .api.serializers import OrderSerializer, OrderItemSerializer
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .utils import send_mail_customer, send_mail_admin



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            send_mail_customer(order.id)
            send_mail_admin(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',{'cart': cart, 'form': form})


class OrderCreatelView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemCreateView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



class OrderDetailView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class OrderItemDetailView(generics.RetrieveUpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
