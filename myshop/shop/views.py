from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import View
from rest_framework import generics
from shop.api.serializers import ProductSerializer


def product_list(request, category_slug=None):
    search_query=request.GET.get('search','')
    if search_query:
        products=Product.objects.filter(Q(name__icontains=search_query)| Q(description__icontains=search_query))
        category = None
    elif category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    elif category_slug == None:
        category = None
        products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()

    paginator=Paginator(products, 12)
    page_number=request.GET.get('page', 1)
    page=paginator.get_page(page_number)
    return render(request,'shop/product/list.html',context={'category': category,
                                                            'categories': categories,
                                                            'products': page,
                                                            'cart_product_form': cart_product_form})


class ProductDetail(View):
    def get(self,request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        cart_product_form = CartAddProductForm()
        return render(request, 'shop/product/detail.html', context={'product': product,
                                                            'cart_product_form': cart_product_form})


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
