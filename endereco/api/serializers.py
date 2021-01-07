from rest_framework.serializers import ModelSerializer
from endereco.models import endereco

class enderecoSerializer(ModelSerializer):
    class Meta:
        model = endereco
        fields = ('linha1', 'linha2', 'estado', 'cidade', 'pais')