from rest_framework import viewsets
from .models import Fotografo, Cliente, Servico, TipoParentesco
from .serializers import FotografoSerializer, ClienteSerializer, ServicoSerializer, TipoParentescoSerializer

class FotografoViewSet(viewsets.ModelViewSet):
    queryset = Fotografo.objects.all()
    serializer_class = FotografoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class TipoParentescoViewSet(viewsets.ModelViewSet):
    queryset = TipoParentesco.objects.all()
    serializer_class = TipoParentescoSerializer