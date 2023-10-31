from django.db import models

from apppedidosnow.models.produto import Produto

class Pedido(models.Model):
    class StatusPedido(models.IntegerChoices):
        PRODUCAO = (1,"Produção",)
        PRONTO = (2,"Pronto",)
        AGUARDANDO = (3, "Aguardando pagamento",)
        FECHADO = (4,"Fechado",)
        
    # usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="pedidos")
    status = models.IntegerField(choices=StatusPedido.choices,  default=StatusPedido.PRODUCAO)
    mesa = models.CharField(max_length=10)
    cliente = models.CharField(max_length=200)

    @property
    def total(self):
        return sum(item.preco_item * item.quantidade for item in self.itens.all())
    
    def __str__(self):
        return f"Pedido {self.pk} ({self.get_status_display()})"
        
class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)
    preco_item = models.DecimalField(max_digits=10, decimal_places=2)