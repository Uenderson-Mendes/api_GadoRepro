from rest_framework import viewsets
from bd.models import Vacas, Usuario, Bezerro, Reprodutor, Prenha
from bd.serializer import VacasSerializer, UsuarioSerializer, BezerroSerializer, ReprodutorSerializer,PrenhaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class VacasViewSet(viewsets.ModelViewSet):
    queryset = Vacas.objects.all()
    serializer_class = VacasSerializer


class BezerroViewSet(viewsets.ModelViewSet):
    queryset = Bezerro.objects.all()
    serializer_class = BezerroSerializer

  


class ReprodutorViewSet(viewsets.ModelViewSet):
    queryset = Reprodutor.objects.all()
    serializer_class = ReprodutorSerializer

class PrenhaViewSet(viewsets.ModelViewSet):
    queryset = Prenha.objects.all()
    serializer_class = PrenhaSerializer
