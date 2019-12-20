from rest_framework import serializers
from shop.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'image', 'description', 'price', 'available')
