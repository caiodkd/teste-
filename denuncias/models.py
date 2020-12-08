from django.db import models

class Denuncia(models.Model):
    cpf = models.CharField (max_length=100)
    depoimento = models.CharField (max_length=500)
    empresa = models.CharField (max_length=100)
    local = models.CharField (max_length=100)
    hora = models.CharField (max_length=100)

class Tipo(models.Model):
    trabalho_escravo = models.CharField (max_length=100)
    assedio = models.CharField (max_length=100)
    discriminacao = models.CharField (max_length=100)
    outros = models.CharField (max_length=100)

class Usuario(models.Model):
    cpf = models.CharField (max_length=100)
    nome = models.CharField (max_length=100)
    data_de_nascimento = models.CharField (max_length=100)
    cep = models.CharField (max_length=100)


    def __str__(self):
        return self.cpf



