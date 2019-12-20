from django.urls import path
from .views import product_list, ProductDetail


app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<category_slug>/', product_list, name='product_list_by_category'),
    path('<id>/<slug>/', ProductDetail.as_view(), name='product_detail'),
]
