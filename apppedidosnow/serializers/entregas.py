from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apppedidosnow.models import Produto, Bairro, Motoboy, Entrega, ItensEntrega

class ItensEntregaSerializer(ModelSerializer):
    class Meta:
        model = ItensEntrega
        fields = ("produto", "quantidade", "preco_item")

class CriarEditarItensEntregaSerializer(ModelSerializer):
    class Meta:
        model = ItensEntrega
        fields = ("produto", "quantidade")

class EntregaSerializer(ModelSerializer):
    itens_entrega = ItensEntregaSerializer(many=True, read_only=True)

    class Meta:
        model = Entrega
        fields = ("id", "cliente", "bairro", "motoboy", "endereco", "taxa_entrega", "status", "itens_entrega")

class CriarEditarEntregaSerializer(ModelSerializer):
    itens_entrega = CriarEditarItensEntregaSerializer(many=True, write_only=True)

    class Meta:
        model = Entrega
        fields = ("cliente", "bairro", "motoboy", "endereco", "itens_entrega")

    def create(self, validated_data):
        itens_entrega_data = validated_data.pop('itens_entrega')
        entrega = Entrega.objects.create(**validated_data)

        for item_data in itens_entrega_data:
            ItensEntrega.objects.create(entrega=entrega, **item_data)

        return entrega