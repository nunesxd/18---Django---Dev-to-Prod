from django.shortcuts import redirect, render


def register(request):
    if request.method == 'POST':
        print('Form Submitted !')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        print('Form Submitted !')

    return render(request, 'accounts/login.html')


def logout():
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
