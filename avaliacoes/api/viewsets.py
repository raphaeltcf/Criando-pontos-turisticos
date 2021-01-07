from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import avaliacoes
from .serializers import avaliacoesSerializer

class avaliacoesViewSet(ModelViewSet):
    queryset = avaliacoes.objects.all()
    serializer_class = avaliacoesSerializer