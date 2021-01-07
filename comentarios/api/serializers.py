from rest_framework.serializers import ModelSerializer
from comentarios.models import comentario

class comentarioSerializer(ModelSerializer):
    class Meta:
        model = comentario
        fields = ('usario', 'comentario', 'data', 'aprovado')