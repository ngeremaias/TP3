from django.db import models
from django.contrib.auth.models import User

class TipoParentesco(models.Model):
    tipo = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.tipo

class Fotografo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.usuario.get_full_name()

class Cliente(models.Model):
    fotografo = models.ForeignKey(Fotografo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    indicado_por = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    parentesco = models.ForeignKey(TipoParentesco, on_delete=models.SET_NULL, null=True, blank=True)
    parente_de = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='clientes_relacionados')
    
    def __str__(self):
        return self.nome

class Servico(models.Model):
    SITUACAO_CHOICES = [
        ('agendado', 'Agendado'),
        ('realizado', 'Realizado'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado'),
    ]
    
    fotografo = models.ForeignKey(Fotografo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_servico = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHOICES, default='agendado')
    data_pagamento = models.DateField(null=True, blank=True)
    observacoes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.descricao} - {self.cliente.nome}"