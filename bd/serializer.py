from rest_framework import serializers
from .models import Usuario, Vacas, Bezerro, Reprodutor,Prenha

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class VacasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacas
        fields = fields = '__all__'

class BezerroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bezerro
        fields = fields = '__all__'

class ReprodutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reprodutor
        fields = fields = '__all__'
class PrenhaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prenha
        fields = '__all__'



   