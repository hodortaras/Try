from django.urls import path
from orders.views import *


app_name = 'api_orders'

urlpatterns = [
    path('create/', OrderCreatelView.as_view()),
    path('create/products/', OrderItemCreateView.as_view()),
    path('<pk>/', OrderDetailView.as_view(), name='order_api'),
    path('item/<pk>/', OrderItemDetailView.as_view(), name='order_detail_api'),
]
