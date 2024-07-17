from django.db import models
from datetime import timedelta

 #info dos users
class User_Admin(models.Model):
   
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
#Tabela Info de Idoso
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
    cpf = models.CharField(max_length=11, unique=True)
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

#Tabela de Atendimento
class Atendimento(models.Model):
    cpf_idoso = models.ForeignKey(Idoso_Dados, on_delete=models.CASCADE, to_field='cpf')
    data = models.DateField()

    pas_1 = models.CharField(max_length=7)
    pad_1 = models.CharField(max_length=7)
    pas_2 = models.CharField(max_length=7)
    pad_2 = models.CharField(max_length=7)
    pas_3 = models.CharField(max_length=7)
    pad_3 = models.CharField(max_length=7)

    frequencia_card = models.PositiveSmallIntegerField()
    saturacao_oxg = models.PositiveSmallIntegerField()
    
    QUALIDADE_SONO_CHOICE = [
        ('Muito ruim', 'Muito ruim'),
        ('Ruim', 'Ruim'),
        ('Regular', 'Regular'),
        ('Bom', 'Bom'),
        ('Muito bom', 'Muito bom'),
    ]
    qualidade_sono = models.CharField(
        max_length=10,
        choices=QUALIDADE_SONO_CHOICE
    )

    BEM_ESTAR_CHOICES = [
        ('Muito ruim', 'Muito ruim'),
        ('Ruim', 'Ruim'),
        ('Regular', 'Regular'),
        ('Bom', 'Bom'),
        ('Muito bom', 'Muito bom'),
    ]
    bem_estar = models.CharField(
        max_length=10,
        choices=BEM_ESTAR_CHOICES
    )

    DOR_CHOICES = [
        ('Sem dor', 'Sem dor'),
        ('Dor leve', 'Dor leve'),
        ('Dor moderada', 'Dor moderada'),
        ('Dor intensa', 'Dor intensa'),
        ('Pior dor possível', 'Pior dor possível'),
    ]
    pain = models.CharField(
        max_length=20,
        choices=DOR_CHOICES
    )

    def __str__(self):
        return f"{self.cpf_idoso.nome} - {self.data}"

#Tabela para treino
class Treino(models.Model):
    cpf_idoso = models.ForeignKey(Idoso_Dados, on_delete=models.CASCADE, to_field='cpf')
    data = models.DateField()

    treino_pres = models.CharField(max_length=20)
    tempo_pres = models.PositiveSmallIntegerField()
    distancia_pres = models.PositiveSmallIntegerField()
    tempo_exec = models.PositiveSmallIntegerField()
    distancia_exec = models.FloatField()

    def __str__(self):
        return f"{self.cpf_idoso.nome} - {self.data}"

#Tabela de Exames
class Exame(models.Model):
    cpf_idoso = models.ForeignKey(Idoso_Dados, on_delete=models.CASCADE, to_field='cpf')
    title = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return f"{self.cpf_idoso.nome} - {self.uploaded_at}"
    
    
 