from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # Testando os alertas de erro de nosso site:
        # messages.error(request, 'Testing error message')
        # return redirect('register')

        # Obtendo os valores dos campos do form:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Checagens dos campos:
        if password != password2:
            messages.error(request, 'Password do not match')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username is already taken')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email is already registered')
            # Apenas a última checagem tem o return, para que os erros sejam acumulativos.
            return redirect('register')

        # Se tudo estiver correto, cria o usuário com os dados fornecidos:
        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        # OPCIONAL - Login após o registro do usuário:
        auth.login(request, user)
        #messages.success(request, 'You are now logged in')
        return redirect('index')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            #messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out, please login again')
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
