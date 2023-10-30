from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from apppedidosnow.models import Entrega
from apppedidosnow.serializers import EntregaSerializer


class EntregaViewSet(ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["endereco", "bairro__nome", "motoboy__nome"]
    search_fields = ["endereco", "bairro__nome", "motoboy__nome"]
    ordering_fields = ["endereco", "bairro__nome", "motoboy__nome"]
    ordering = ["endereco"]