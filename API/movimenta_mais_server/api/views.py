from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User_Admin
from .serializers import User_AdminSerializer
from rest_framework.views import APIView


class User_AdminListCreate(generics.ListCreateAPIView):
    """"Cria um novo admin e retorna tds os admins"""
    queryset = User_Admin.objects.all()
    serializer_class = User_AdminSerializer
    
    """"Para deletar todos os usuários_admin"""
    def delete(self, request, *args,**kwargs):
        User_Admin.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def options(self, request, *args, **kwargs):
        """Trata as opções de pré-voo do CORS."""
        return Response()
    def post(self, request, *args, **kwargs):
        """Cria um novo usuário administrador."""
        serializer = User_AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class User_AdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """"Permite apagar e edit o user_admin"""
    queryset = User_Admin.objects.all()
    serializer_class = User_AdminSerializer
    lookup_field = "pk" 
    
    def put(self, request, *args, **kwargs):
        """Atualiza um usuário administrador por ID."""
        instance = self.get_object()
        serializer = User_AdminSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, *args, **kwargs):
        """Atualiza parcialmente um usuário administrador por ID."""
        instance = self.get_object()
        serializer = User_AdminSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class User_AdminList(APIView):
    #FUNÇÃO GET
    def get(self, request, format=None):
        nome = request.query_params.get("nome","")
        
        if nome:
            users = User_Admin.objects.filter(nome_icontains= nome)
        else:
            users = User_Admin.objects.all()
            
        serializer = User_AdminSerializer(users, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)