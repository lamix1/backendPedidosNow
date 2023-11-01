from django.db import models

class Funcionario(models.Model):
    login = models.CharField(max_length=10, default=0, null=True, blank=True)
    nome = models.CharField(max_length=100, default=0, null=True, blank=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome
