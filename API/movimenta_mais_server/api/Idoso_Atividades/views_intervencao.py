from rest_framework import generics

from ..serializers import Pos_IntervencaoSerializer, Pre_IntervencaoSerializer
from ..models import Pos_Intervencao, Pre_Intervencao

#todo(Ana: atualizar informações de pre e pos)

#cria e lista os registos de pre-intervenção
class Pre_IntervencaoListCreate(generics.ListCreateAPIView):
  queryset = Pre_Intervencao.objects.all()
  serializer_class = Pre_IntervencaoSerializer

#cria e lista os registos de pos-intervenção
class Pos_IntervencaoListCreate(generics.ListCreateAPIView):
  queryset = Pos_Intervencao.objects.all()
  serializer_class = Pos_IntervencaoSerializer  



