from django.db import models
from django.contrib.auth.models import AbstractUser

class: Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length=100)
    idade = models.ImageField('Idade')
    email = models.EmailField('Email')
    matricula = models.CharField('Matricula', max_length=14)
    telofone = models.CharField('Telefone', max_length=12)

USERNAME_FILED = 'Nome' 

# Create your models here.
