from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reservation
from events.models import Event
from users.models import User

def reservation_create(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')
        participant_count = int(request.POST['participant_count'])
        Reservation.objects.create(
            user_id=user_id,
            event=event,
            participant_count=participant_count
        )
        messages.success(request, 'Rezervasyon oluşturuldu.')
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_create.html', {'event': event})

def reservation_list(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    reservations = Reservation.objects.filter(user_id=user_id)
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def reservation_cancel(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.status = 'cancelled'
    reservation.save()
    messages.success(request, 'Rezervasyon iptal edildi.')
    return redirect('reservation_list')