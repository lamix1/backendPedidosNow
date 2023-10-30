from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from apppedidosnow.models import Bairro
from apppedidosnow.serializers import BairroSerializer


class BairroViewSet(ModelViewSet):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["nome"]
    search_fields = ["nome"]
    ordering_fields = ["nome", "preco_entrega"]
    ordering = ["nome"]