from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from apppedidosnow.models import Motoboy
from apppedidosnow.serializers import MotoboySerializer


class MotoboyViewSet(ModelViewSet):
    queryset = Motoboy.objects.all()
    serializer_class = MotoboySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["nome"]
    search_fields = ["nome"]
    ordering_fields = ["nome", "telefone", "email"]
    ordering = ["nome"]