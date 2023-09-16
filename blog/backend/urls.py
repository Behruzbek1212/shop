from django.urls import path
from .views import *

urlpatterns = [
    path('', shop, name='shop'),
    path('shop_single/<slug:slug>/', shop_single, name='shop_single'),
    path('shop_cart/', shop_cart, name='shop_cart'),
    path('shop_checkout/', shop_checkout, name='shop_checkout'),
    path('shop_order_details', shop_order_details),
    path('shop_checkout/',  shop_checkout, name='shop_checkout'),
    path('shop_register/', shop_register, name='shop_register'),
    path('shop_reset_password/', shop_reset_password, name='shop_reset_password'),
    path('page_not_found/', page_not_found, name='page_not_found' ),
   
    
]
