from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # Um retorno que será usado apenas para o teste da criação de nossa rota:
    return HttpResponse('<h1>Hello World</h1>')
