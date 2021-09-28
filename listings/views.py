from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing


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
    return render(request, 'listings/search.html')
