from django.urls import path
from . import views

urlpatterns = [
    # Poderá ser acessada pela rota '/listings'.
    path('', views.index, name='listings'),
    # Queremos passar o parâmetro id do 'listing' pela url.
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
