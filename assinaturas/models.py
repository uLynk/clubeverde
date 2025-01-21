from django.db import models
from usuarios.models import Usuario

class Assinatura(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_plano = models.CharField(max_length=50)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_expiracao = models.DateTimeField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.usuario.nome} - {self.tipo_plano}"
