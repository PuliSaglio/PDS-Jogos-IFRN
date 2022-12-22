from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=100)
    idade = models.ImageField('Idade')
    email = models.EmailField('Email')
    matricula = models.CharField('Matricula', max_length=14, unique=True)
    telofone = models.CharField('Telefone', max_length=12)

    USERNAME_FILED = 'matricula' 

# Create your models here.
