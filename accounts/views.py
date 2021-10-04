from django.shortcuts import redirect, render
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        # Testando os alertas de erro de nosso site:
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Testando os alertas de erro de nosso site:
        messages.error(request, 'Testing error message')
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout():
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
