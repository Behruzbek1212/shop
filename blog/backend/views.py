from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import *


def shop(request):
    post = Post.objects.all()
    
    if 'q' in request.GET:
        q = request.GET['q']
        barchasi = Q(Q(nomi__icontains=q) | Q(hozirgi_narx__icontains=q) | Q(oldingi_narx__icontains=q) | Q(sotuvda_nechta__icontains=q) | 
        Q(tavsif__icontains=q) | Q(barcha_malumotlar__icontains=q) | Q(operativ_xotira__icontains=q) | Q(xotira__icontains=q) | Q(operatsion_tizim__icontains=q) | 
        Q(asosiy_kamera__icontains=q) | Q(old_kamera__icontains=q) | Q(batareya_quvvati__icontains=q) | Q(ekran_dioganali__icontains=q) | Q(protsessor__icontains=q) | Q(brand_nomi__icontains=q)) 
        post = Post.objects.filter(barchasi)

    paginator = Paginator(post, 1)
    page_number = request.GET.get('page', 1)
    project_pagination = paginator.get_page(page_number)
    totalpages = project_pagination.paginator.num_pages
    page_range = paginator.get_elided_page_range(number=page_number)
    
    context = {
        'post': post,
        'post': project_pagination,
        'totalpages': totalpages,
        'page_range': page_range,
        'list_pagination': [n+1 for n in range(totalpages)]
    }
    
    return render(request, 'shop.html',context)

def shop_single(request, slug):
    post = Post.objects.get(slug=slug)
    rasmlar = PostImage.objects.filter(post=post)
    context = {
        'post': post,
        'rasmlar': rasmlar,

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






