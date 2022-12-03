
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    data_nascimento = models.DateField()

class camisa(models.Model):
    tamanho = models.CharField(max_length=3)
    cor = models.CharField(max_length=20)
    preco = models.FloatField()
    tipo = models.CharField(max_length=50)

class sapato(models.Model):
    tamanho = models.IntegerField()
    cor = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    preco = models.FloatField()
    tipo = models.CharField(max_length=3)

class short(models.Model):
    tamanho = models.CharField(max_length=3)
    cor = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    preco = models.FloatField()





