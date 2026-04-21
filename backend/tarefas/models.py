from django.db import models
from tarefas.usuarios.models import Usuario

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTA')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()

    def __str__(self):
        return self.titulo
