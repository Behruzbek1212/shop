from django.shortcuts import render, redirect
from .models import *


def shop(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'shop.html',context)

def shop_single(request, slug):
    post = Post.objects.get(slug==slug)
    context = {
        'post': post
    }
    return render(request, 'shop-single.html', context)


def shop_cart(request):
    return render(request, 'shop-cart.html')

def shop_checkout(request):
    return render(request, 'shop-checkout.html')

def shop_order_details(request):
    return render(request, 'shop-order-details.html')

def shop_checkout(request):
    return render(request, 'shop-checkout.html')


def shop_register(request):
    return render(request, 'shop-register.html')

def shop_reset_password(request):
    return render(request, 'shop-reset-password.html')

def page_not_found(request):
    return render(request, '404.html')