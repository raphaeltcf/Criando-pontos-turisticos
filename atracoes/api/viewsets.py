from rest_framework.viewsets import ModelViewSet
from atracoes.models import atracao
from .serializers import atracaoSerializer


class atracoesViewSet(ModelViewSet):
    queryset = atracao.objects.all()
    serializer_class = atracaoSerializer
    filterset_fields = ['nome', 'idade_minima', 'horario_func']
