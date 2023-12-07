from django.db import models
from apppedidosnow.models import Produto, Bairro, Motoboy

class Entrega(models.Model):
    class StatusEntrega(models.IntegerChoices):
        PENDENTE = (1, "Pendente")
        ENTREGUE = (2, "Entregue")

    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT)
    motoboy = models.ForeignKey(Motoboy, on_delete=models.PROTECT)
    endereco = models.TextField()
    taxa_entrega = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.IntegerField(choices=StatusEntrega.choices, default=StatusEntrega.PENDENTE)
    cliente = models.CharField(max_length=200)

    @property
    def total_com_taxa_entrega(self):
        return self.total + self.bairro.preco_entrega

    @property
    def total(self):
        return sum(item.preco_item * item.quantidade for item in self.itens_entrega.all())

    def __str__(self):
        return f"Entrega {self.pk} ({self.get_status_display()})"


class ItensEntrega(models.Model):
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens_entrega")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1)
    preco_item = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto} - {self.quantidade} unidades"