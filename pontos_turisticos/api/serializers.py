from rest_framework.serializers import ModelSerializer
from pontos_turisticos.models import pontoturistico
from atracoes.api.serializers import atracaoSerializer
from endereco.api.serializers import enderecoSerializer
from comentarios.api.serializers import comentarioSerializer
from avaliacoes.api.serializers import avaliacoesSerializer

class pontoturisticoSerializer(ModelSerializer):
    atracoes = atracaoSerializer(many=True)
    endreco = enderecoSerializer()
    comentarios = comentarioSerializer(many=True)
    avaliacoes = avaliacoesSerializer(many=True)


    class Meta:
        model = pontoturistico
        fields = ['id', 'nome', 'descricao', 'atracoes,','comentarios', 'avaliacoes', 'endereco', 'foto']