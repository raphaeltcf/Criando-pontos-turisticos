from rest_framework.viewsets import ModelViewSet
from comentarios.models import comentario
from .serializers import comentarioSerializer

class comentarioViewSet(ModelViewSet):
    queryset = comentario.objects.all()
    serializer_class = comentarioSerializer