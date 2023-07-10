from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bd.views import VacasViewSet, UsuarioViewSet, BezerroViewSet, ReprodutorViewSet, PrenhaViewSet

router = routers.DefaultRouter()
router.register('usuario', UsuarioViewSet, basename='usuarios')
router.register('vacas', VacasViewSet, basename='vacas')
router.register('bezerros', BezerroViewSet, basename='bezerros')
router.register('reprodutor', ReprodutorViewSet, basename='reprodutor')
router.register('Prenha', PrenhaViewSet, basename='prenha')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
