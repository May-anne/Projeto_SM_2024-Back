from rest_framework import serializers
from .models import Pos_Intervencao, User_Admin, Idoso_Dados, Pre_Intervencao

""""Converte Pra JSON"""
class User_AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Admin
        fields = ["id","nome","senha"]
        

class Idoso_DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idoso_Dados
        fields = "__all__"

class Pre_IntervencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pre_Intervencao
        fields = "__all__"        

class Pos_IntervencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_Intervencao
        fields = "__all__"

    def validate(self, data):
        user = data['user']
        data_intervencao = data['data']        
        existe_pre = Pre_Intervencao.objects.filter(
            user=user,
            data=data_intervencao
        ).exists()

        if not existe_pre:
            raise serializers.ValidationError("O registro de Pre Intervenção correspondente não existe.")

        return data
