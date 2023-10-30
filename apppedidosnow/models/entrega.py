from django.db import models

from apppedidosnow.models import Bairro, Motoboy

class Entrega(models.Model):

    endereco = models.CharField(max_length=200)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, null=True, blank=True)
    motoboy = models.ForeignKey(Motoboy, on_delete=models.CASCADE, null=True, blank=True)