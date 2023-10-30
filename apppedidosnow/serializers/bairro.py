from rest_framework.serializers import ModelSerializer

from apppedidosnow.models import Bairro

class BairroSerializer(ModelSerializer):
    class Meta:
        model = Bairro
        fields = "__all__"