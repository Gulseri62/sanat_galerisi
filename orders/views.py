from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, Payment, Coupon
from artworks.models import Artwork

def order_create(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')
        method = request.POST['method']
        order = Order.objects.create(
            user_id=user_id,
            artwork=artwork,
            total_price=artwork.price
        )
        Payment.objects.create(
            order=order,
            method=method,
            amount=artwork.price
        )
        messages.success(request, 'Satın alma başarılı.')
        return redirect('order_list')
    return render(request, 'orders/order_create.html', {'artwork': artwork})

def order_list(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    orders = Order.objects.filter(user_id=user_id)
    return render(request, 'orders/order_list.html', {'orders': orders})
