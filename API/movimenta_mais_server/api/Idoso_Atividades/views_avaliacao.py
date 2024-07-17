from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Avaliacao, Idoso_Dados
from ..serializers import AvaliacaoSerializer

class AvaliacaoCreateAPIView(generics.CreateAPIView):
  queryset = Avaliacao.objects.all()
  serializer_class = AvaliacaoSerializer
  
  def post(self, request):
    cpf = request.data.get('cpf_idoso')
    if cpf:
      try:
        idoso = Idoso_Dados.objects.get(cpf=cpf)
        request.data['cpf_idoso'] = idoso.cpf
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      except Idoso_Dados.DoesNotExist:
        return Response({"detail": "Idoso não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    return Response({"detail": "CPF não fornecido."}, status=status.HTTP_400_BAD_REQUEST)
  
class AvaliacaoRetrieverUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Avaliacao.objects.all()
  serializer_class = AvaliacaoSerializer
  lookup_field = 'pk' 

  def put(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      serializer = AvaliacaoSerializer(instance, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
    except:    
      return Response({"detail": "Requisição inválida."}, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, *args, **kwargs):
    try:
      instance = self.get_object() 
      instance.delete()
      return Response({"detail": "Avaliação deletada com sucesso."}, status=status.HTTP_204_NO_CONTENT)    
    except:
      return Response({"detail": "Requisição inválida."}, status=status.HTTP_400_BAD_REQUEST)

class AvaliacaoList(APIView):
  def get(self, request, format=None):
    cpf = request.query_params.get('cpf')
    if cpf:
        atendimentos = Avaliacao.objects.filter(cpf_idoso__cpf=cpf)
        if atendimentos.exists():
          serializer = AvaliacaoSerializer(atendimentos, many=True)
          return Response(serializer.data, status=status.HTTP_200_OK)
        else:
          return Response({"detail": "Avaliações não encontradas para o cpf fornecido."}, status=status.HTTP_404_NOT_FOUND) 
    else:
      treinos = Avaliacao.objects.all() 
      serializer = AvaliacaoSerializer(treinos, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
      
