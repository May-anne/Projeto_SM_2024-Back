from rest_framework import serializers
from .models import User_Admin, Idoso_Dados

""""Converte Pra JSON"""
class User_AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Admin
        fields = ["id","nome","senha"]
        

class Idoso_DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idoso_Dados
        fields = "__all__"