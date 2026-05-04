from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Review, Favorite, SupportTicket
from artworks.models import Artwork
from events.models import Event

def add_review(request, artwork_id=None, event_id=None):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        Review.objects.create(
            user_id=user_id,
            artwork_id=artwork_id,
            event_id=event_id,
            rating=rating,
            comment=comment
        )
        messages.success(request, 'Yorumunuz eklendi.')
        if artwork_id:
            return redirect('artwork_detail', pk=artwork_id)
        return redirect('event_detail', pk=event_id)
    return render(request, 'reviews/add_review.html')

def add_favorite(request, artwork_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    Favorite.objects.get_or_create(user_id=user_id, artwork_id=artwork_id)
    return redirect('artwork_detail', pk=artwork_id)

def remove_favorite(request, artwork_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    Favorite.objects.filter(user_id=user_id, artwork_id=artwork_id).delete()
    return redirect('artwork_detail', pk=artwork_id)

def favorite_list(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    favorites = Favorite.objects.filter(user_id=user_id)
    return render(request, 'reviews/favorite_list.html', {'favorites': favorites})

def support_ticket_create(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        SupportTicket.objects.create(
            user_id=user_id,
            subject=subject,
            message=message
        )
        messages.success(request, 'Talebiniz iletildi.')
        return redirect('home')
    return render(request, 'reviews/support_ticket.html')