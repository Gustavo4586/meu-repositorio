from unittest.util import _MAX_LENGTH
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(_MAX_LENGTH=100)
    idade = models.IntegerField()
    email = models.EmailField()
    data_nascimento = models.DateField()

class camisa(models.Model):
    tamanho = models.CharField(_MAX_LENGTH=3)
    cor = models.CharField(_MAX_LENGTH=20)
    preco = models.FloatField()
    tipo = models.CharField(_MAX_LENGTH=50)

class sapato(models.Model):
    tamanho = models.IntegerField()
    cor = models.CharField(_MAX_LENGTH=20)
    marca = models.CharField(_MAX_LENGTH=50)
    preco = models.FloatField()
    tipo = models.CharField()

class short(models.Model):
    tamanho = models.CharField(_MAX_LENGTH=3)
    cor = models.CharField(_MAX_LENGTH=20)
    marca = models.CharField(_MAX_LENGTH=50)
    preco = models.FloatField()





