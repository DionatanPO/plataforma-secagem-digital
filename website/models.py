from django.db import models

class Orcamento(models.Model):
    nome_completo = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    descricao = models.TextField()
    prazo = models.DateField()
    orcamento_disponivel = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome_completo} - {self.orcamento_disponivel}"

    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"
