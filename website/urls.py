
from django.urls import path, include
from . import views
from .api.viewsets import OrcamentoViewSet
from rest_framework import  routers

routers = routers.DefaultRouter()

routers.register(r'orcamentos', OrcamentoViewSet, basename='orcamentos')

urlpatterns = [
    path('api/', include(routers.urls)),
    path('', views.index, name='index'),
    path('portifolio', views.portifolio, name='portifolio'),
    path('equipe', views.equipe, name='equipe'),
    path('centro', views.centro, name='centro'),
    path('iot', views.iot, name='iot'),
    path('sobre', views.sobre, name='sobre'),
    path('contato', views.contato, name='contato'),
    path('cursos', views.cursos, name='cursos'),
    path('servicos', views.servicos, name='servicos'),
    path('politica_privacidade', views.politica_privacidade, name='politica_privacidade'),
    path('politica_privacidade2', views.politica_privacidade2, name='politica_privacidade2'),
    path('politica_privacidade_rondo_move', views.politica_privacidade3, name='politica_privacidade3'),

    path('page1', views.page1, name='page1'),
    path('page2/<str:turno_id>/', views.page2, name='page2'),
    path('page3', views.page3, name='page3'),

    path('documentario', views.documentario, name='documentario'),
    path('dionatan', views.dionatan, name='dionatan'),
]