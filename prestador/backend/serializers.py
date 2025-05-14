from rest_framework import serializers
from .models import Fotografo, Cliente, Servico, TipoParentesco

class TipoParentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoParentesco
        fields = '__all__'

class FotografoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotografo
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'