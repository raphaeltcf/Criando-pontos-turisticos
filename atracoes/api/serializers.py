from rest_framework.serializers import ModelSerializer
from atracoes.models import atracao

class atracaoSerializer(ModelSerializer):
    class Meta:
        model = atracao
        fields = ('nome', 'descricao', 'horario_func', 'idade_minima', 'foto')
