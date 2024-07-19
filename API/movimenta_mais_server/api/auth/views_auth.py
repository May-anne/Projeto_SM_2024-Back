from ..models import User_Admin
from ..serializers import User_AdminSerializer

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import jwt
import datetime
from django.conf import settings

# Cria e lista usuários admin (C e R do CRUD)
class User_AdminListCreate(generics.ListCreateAPIView):
    queryset = User_Admin.objects.all()
    serializer_class = User_AdminSerializer

    def delete(self, request, *args, **kwargs):
        """Deleta todos os usuários_admin"""
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

# Recupera, atualiza e deleta usuários admin por ID (R, U, D do CRUD)    
class User_AdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
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

# Lista usuários e admin
class User_AdminList(APIView):
    def get(self, request, format=None):
        """Retorna uma lista de usuários"""
        nome = request.query_params.get("nome", "")
        
        if nome:
            users = User_Admin.objects.filter(nome__icontains=nome)
        else:
            users = User_Admin.objects.all()
            
        serializer = User_AdminSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Função de login
@api_view(['POST'])
def sign_in(request):
    login = request.data.get('nome')
    password = request.data.get('senha')
    
    if not login or not password: #Caso campos estejam vazios
        return Response({"error": "Login e senha são necessários."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:#tenta encontrar user name
        user = User_Admin.objects.get(nome=login) 
    except User_Admin.DoesNotExist:
        return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if password == user.senha: #verifica se a senha é correta
        # Cria o token JWT
        token = create_token({"nome": user.nome}, settings.SECRET_KEY)
        #serializer = User_AdminSerializer(user)
        return Response({"token": token}, status=status.HTTP_200_OK) #Retorna o Token
    else:
        return Response({"error": "Senha inválida."}, status=status.HTTP_401_UNAUTHORIZED) 

# Função p/criar token JWT
def create_token(data, secret_key):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({'data': data, 'exp': expiration}, secret_key, algorithm='HS256')
    return token
