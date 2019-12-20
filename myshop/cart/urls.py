from django.urls import path
from .views import CartDetail, cart_add, cart_remove
from django.conf.urls import url

app_name = 'cart'

urlpatterns = [
    path('', CartDetail.as_view(), name='cart_detail'),
    path('add/<product_id>', cart_add, name='cart_add'),
    path('remove/<product_id>', cart_remove, name='cart_remove'),
]
