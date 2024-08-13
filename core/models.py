from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=100, unique=True)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to="alunos/")