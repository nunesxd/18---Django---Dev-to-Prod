from django.shortcuts import render
from django.http import HttpResponse
# Mesmo do módulo 'pages' podemos importar o ORM de 'listings' e usá-lo:
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    # Um retorno que será usado apenas para o teste da criação de nossa rota:
    # return HttpResponse('<h1>Hello World</h1>')

    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        "listings": listings
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Pega todos os vendedores:
    realtors = Realtor.objects.order_by('-hire_date')
    # Pega apenas o MVP:
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        "realtors": realtors,
        "mvp_realtors": mvp_realtors
    }

    return render(request, 'pages/about.html', context)
