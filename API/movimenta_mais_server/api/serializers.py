from rest_framework import serializers
from .models import  Treino, User_Admin, Idoso_Dados, Atendimento

#Converte Pra JSON

#Users e ADM
class User_AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Admin
        fields = ["id","nome","senha"]
        
#Dados Idosos
class Idoso_DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idoso_Dados
        fields = "__all__"


#Dados de Atendimento
class AtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendimento
        fields = "__all__"        

#Dados de
class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treino
        fields = "__all__"      

       