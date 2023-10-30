from rest_framework.serializers import ModelSerializer

from apppedidosnow.models import Entrega

class EntregaSerializer(ModelSerializer):
    class Meta:
        model = Entrega
        fields = "__all__"