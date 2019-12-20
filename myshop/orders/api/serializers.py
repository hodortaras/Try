from rest_framework import serializers
from orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('first_name', 'region', 'city', 'adress', 'coment')
