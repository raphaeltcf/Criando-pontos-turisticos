import token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import pontoturistico
from .serializers import pontoturisticoSerializer

class pontoturisticoViewSet(ModelViewSet):

    queryset = pontoturistico.objects.all()
    serializer_class = pontoturisticoSerializer
    permission_classes = [DjangoModelPermissions]
    authentication_classes = (TokenAuthentication)