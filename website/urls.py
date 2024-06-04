from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portifolio', views.portifolio, name='portifolio'),
    path('equipe', views.equipe, name='equipe'),
    path('sobre', views.sobre, name='sobre'),
    path('contato', views.contato, name='contato'),
    path('cursos', views.cursos, name='cursos'),
    path('servicos', views.servicos, name='servicos'),
    path('politica_privacidade', views.politica_privacidade, name='politica_privacidaDE'),
]