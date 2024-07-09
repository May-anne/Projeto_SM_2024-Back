from django.db import models

 #info dos users
class User_Admin(models.Model):
   
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
#Info de cadastro dos idosos 
class Idoso_Dados(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1)
    raca = models.CharField(max_length=20)
    escolaridade = models.CharField(max_length=50)
    deficiencia = models.BooleanField()
    deficiencia_quais = models.TextField(max_length=500)
    telefone_pessoal = models.CharField(max_length=11)
    telefone_emergencial = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    cartao_cns = models.CharField(max_length=15)
    plano_saude = models.BooleanField()
    plano_saude_qual = models.CharField(max_length=50, blank=True, null=True)  # Adicione blank=True, null=True se plano_saude for False
    onde_moras = models.CharField(max_length=50)
    com_quem_mora = models.TextField(max_length=200)
    quantos_residem = models.PositiveSmallIntegerField()
    meio_transporte = models.CharField(max_length=50)
    situacao_economica = models.CharField(max_length=50)
    renda = models.IntegerField()
    problemas_saude = models.BooleanField()
    problemas_saude_quais = models.TextField(max_length=500, blank=True, null=True)  # Adicione blank=True, null=True se problemas_saude for False
    cirgurgia_recente = models.BooleanField()
    cirurgia_quais = models.TextField(max_length=500, blank=True, null=True)  # Adicione blank=True, null=True se cirgurgia_recente for False
    internacao_recente = models.BooleanField()
    internacao_quais = models.TextField(max_length=500, blank=True, null=True)  # Adicione blank=True, null=True se internacao_recente for False
    alcool = models.BooleanField()
    fumante = models.BooleanField()
    drogas = models.BooleanField()
    medicamentos = models.BooleanField()
    medicamentos_quais = models.TextField(max_length=200, blank=True, null=True)  # Adicione blank=True, null=True se medicamentos for False
    
    def __str__(self):
        return self.nome
   