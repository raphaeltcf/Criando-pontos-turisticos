from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from pontos_turisticos.api.viewsets import pontoturisticoViewSet
from atracoes.api.viewsets import atracoesViewSet
from endereco.api.viewsets import enderecoViewSet
from comentarios.api.viewsets import comentarioViewSet
from avaliacoes.api.viewsets import avaliacoesViewSet
from rest_framework.authtoken import views



router = routers.DefaultRouter()
router.register(r'pontoturistico', pontoturisticoViewSet)
router.register(r'atracoes', atracoesViewSet)
router.register(r'endereco', enderecoViewSet)
router.register(r'comentario', comentarioViewSet)
router.register(r'avaliacoes', avaliacoesViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
]
