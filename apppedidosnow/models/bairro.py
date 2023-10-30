from django.db import models

class Bairro(models.Model):
    nome = models.CharField(max_length=255, default=0, null=True, blank=True)
    preco_entrega = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    
    def __str__(self):
        return self.nome