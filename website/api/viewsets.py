from rest_framework import viewsets
from .serializers import OrcamentoSerializer
from ..models import Orcamento

class OrcamentoViewSet(viewsets.ModelViewSet):
    queryset = Orcamento.objects.all()
    serializer_class = OrcamentoSerializer
