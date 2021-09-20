from django.contrib import admin
from .models import Listing

# Estamos adicionando o modelo de 'Listing' ao nossos admins, de forma que eles podem manipulá-los.
admin.site.register(Listing)
