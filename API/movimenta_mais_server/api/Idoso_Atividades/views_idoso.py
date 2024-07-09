from ..models import Idoso_Dados
from ..serializers import Idoso_DadosSerializer

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Cria e lista os formulários de idosos (C e R do CRUD)
class Idoso_DadosListCreate(generics.ListCreateAPIView):
    queryset = Idoso_Dados.objects.all()
    serializer_class = Idoso_DadosSerializer

# View para deletar todos os registros de Idoso_Dados
class Idoso_DadosDeleteAll(APIView):
    def delete(self, request, *args, **kwargs):
        """Deleta todos os Idoso_Dados"""
        Idoso_Dados.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Recupera, atualiza e deleta usuários admin por ID (R, U, D do CRUD)    
class Idoso_DadosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idoso_Dados.objects.all()
    serializer_class = Idoso_DadosSerializer
    lookup_field = "pk"

    def put(self, request, *args, **kwargs):
        """Atualiza um usuário administrador por ID."""
        instance = self.get_object()
        serializer = Idoso_DadosSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, *args, **kwargs):
        """Atualiza parcialmente um usuário administrador por ID."""
        instance = self.get_object()
        serializer = Idoso_DadosSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Lista usuários e admin
class Idoso_DadosList(APIView):
    def get(self, request, format=None):
        """Retorna uma lista de usuários"""
        nome = request.query_params.get("nome", "")
        
        if nome:
            users = Idoso_Dados.objects.filter(nome__icontains=nome)
        else:
            users = Idoso_Dados.objects.all()
            
        serializer = Idoso_DadosSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
