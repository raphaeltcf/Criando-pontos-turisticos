from rest_framework.serializers import ModelSerializer
from avaliacoes.models import avaliacoes

class avaliacoesSerializer(ModelSerializer):
    class Meta:
        model = avaliacoes
        fields = ('user', 'comentario', 'nota', 'data')