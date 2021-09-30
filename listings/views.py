from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # Paginação, total de 6 itens por página:
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    # Criamos um dicionário para passar os dados que queremos aos templates abaixo:
    context = {
        "listings": paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    # Como cada imóvel pode, ou não, ter as 6 fotos possíveis, pensamos em verificar inicialmente no BD e depois passar o objeto para o template, de forma separada do listing.
    other_photos = []
    for n in range(1, 7):
        try:
            other_photos.append(getattr(listing, f'photo_{n}').url)
        except ValueError:
            continue

    context = {
        "listing": listing,
        "other_photos": other_photos
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Verifica se o campo 'keywords' foi preenchido:
    if 'keywords' in request.GET:
        # Obtém o conteúdo do que foi passado pelo método GET:
        keywords = request.GET['keywords']
        # Verifica se por acaso não está vazio:
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # Verifica se o campo 'city' foi preenchido:
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # Verifica se o campo 'state' foi preenchido:
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)

    # Verifica se o campo 'bedrooms' foi preenchido:
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)

    # Verifica se o campo 'price' foi preenchido:
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    context = {
        "listings": queryset_list,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices
    }

    return render(request, 'listings/search.html', context)
