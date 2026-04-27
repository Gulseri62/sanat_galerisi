from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Bu email zaten kayıtlı.')
            return redirect('register')

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        return redirect('login')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            return redirect('home')
        except User.DoesNotExist:
            messages.error(request, 'Email veya şifre hatalı.')
            return redirect('login')

    return render(request, 'users/login.html')


def logout_view(request):
    request.session.flush()
    return redirect('login')
