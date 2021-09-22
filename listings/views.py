from django.shortcuts import render
from .models import Listing


def index(request):
    listings = Listing.objects.all

    # Criamos um dicionário para passar os dados que queremos aos templates abaixo:
    context = {
        "listings": listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
