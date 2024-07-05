from django.db import models

class User_Admin(models.Model):
    """"Tabela de Admins"""
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
    
    
    
