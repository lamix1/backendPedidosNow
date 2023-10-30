from rest_framework.serializers import ModelSerializer

from apppedidosnow.models import Motoboy

class MotoboySerializer(ModelSerializer):
    class Meta:
        model = Motoboy
        fields = "__all__"