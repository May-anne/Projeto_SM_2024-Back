from rest_framework import serializers
from .models import User_Admin

""""Converte Pra JSON"""
class User_AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Admin
        fields = ["id","nome"]