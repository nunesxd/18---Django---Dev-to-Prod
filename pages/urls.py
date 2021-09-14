from django.urls import path
from . import views

urlpatterns = [
    # Associamos o método 'index' de 'views' a raiz de nosso site, o terceiro parâmetro é apenas um nome para simplificar o processo.
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
