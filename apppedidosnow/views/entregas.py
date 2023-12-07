from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from apppedidosnow.models import Entrega
from apppedidosnow.serializers import EntregaSerializer, CriarEditarEntregaSerializer


class EntregaViewSet(ModelViewSet):
    queryset = Entrega.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status"]
    search_fields = ["status"]
    ordering_fields = ["status"]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return EntregaSerializer
        return CriarEditarEntregaSerializer