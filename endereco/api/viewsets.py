from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from endereco.models import endereco
from .serializers import enderecoSerializer

class enderecoViewSet(ModelViewSet):
    queryset = endereco.objects.all()
    serializer_class = enderecoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['estado', 'cidade', 'pais']

