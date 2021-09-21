from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    # O que estiver em parênteses irá aparecer como coluna em nossa tabela no admin:
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    # Este atributo permitirá entrar no elemento clicando nele, por padrão apenas o primeiro elemento permite isto, no caso o 'id' definido acima.
    list_display_links = ('id', 'title')
    # Funcionalidade filtragem as colunas selecionadas:
    list_filter = ('realtor',)
    # Funcionalidade de edição das colunas selecionadas:
    list_editable = ('is_published',)
    # Funcionalidade de procurar, search, nas colunas selecionadas:
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode', 'price')
    # Funcionalidade de paginação:
    list_per_page = 25


# Estamos adicionando o modelo de 'Listing' ao nossos admins, de forma que eles podem manipulá-los.
admin.site.register(Listing, ListingAdmin)
