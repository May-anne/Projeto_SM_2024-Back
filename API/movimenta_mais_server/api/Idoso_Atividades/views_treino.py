from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from ..models import Idoso_Dados, Treino
from ..serializers import TreinoSerializer


class TreinoCreateAPIView(generics.CreateAPIView):
  queryset = Treino.objects.all()
  serializer_class = TreinoSerializer 

  def post(self, request):
    cpf = request.data.get('cpf_idoso')
    if cpf:
      try:
        idoso = Idoso_Dados.objects.get(cpf=cpf)
        request.data['cpf_idoso'] = idoso.cpf
        serializer = TreinoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      except Idoso_Dados.DoesNotExist:
        return Response({"detail": "Idoso não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    return Response({"detail": "CPF não fornecido."}, status=status.HTTP_400_BAD_REQUEST)

class TreinoList(APIView):
  def get(self, request, format=None):
    cpf = request.query_params.get('cpf')
    if cpf:
        treinos = Treino.objects.filter(cpf_idoso__cpf=cpf)
        if treinos.exists():
          serializer = TreinoSerializer(treinos, many=True)
          return Response(serializer.data, status=status.HTTP_200_OK)
        else:
          return Response({"detail": "Treinos não encontrados para o cpf fornecido."}, status=status.HTTP_404_NOT_FOUND) #retorna os treinos do cpf 
    else:
      treinos = Treino.objects.all() 
      serializer = TreinoSerializer(treinos, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK) #retorna todos os treinos 

      
class TreinoRetrieverUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Treino.objects.all()
  serializer_class = TreinoSerializer
  lookup_field = 'pk' 

  def put(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      serializer = TreinoSerializer(instance, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
    except:    
      return Response({"detail": "Requisição inválida."}, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, *args, **kwargs):
    try:
      instance = self.get_object() 
      instance.delete()
      return Response({"detail": "Treino deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)    
    except:
      return Response({"detail": "Requisição inválida."}, status=status.HTTP_400_BAD_REQUEST)
