from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from ..models import Treino
from ..serializers import TreinoSerializer


class TreinoCreateAPIView(generics.CreateAPIView):
  queryset = Treino.objects.all()
  serializer_class = TreinoSerializer 

class TreinoList(APIView):
    def get(self, request, format=None):
      cpf = request.query_params.get('cpf')
      if cpf:
          treinos = Treino.objects.filter(cpf_idoso__cpf=cpf)
          if treinos.exists():
              serializer = TreinoSerializer(treinos, many=True)
              return Response(serializer.data, status=status.HTTP_200_OK)
          else:
              return Response({"detail": "Treinos não encontrados."}, status=status.HTTP_404_NOT_FOUND)
      else:
          return Response({"detail": "CPF não fornecido."}, status=status.HTTP_400_BAD_REQUEST)
   
class TreinoRetrieverUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Treino.objects.all()
  serializer_class = TreinoSerializer
  lookup_field = 'pk' 
