from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import AtendimentoSerializer
from ..models import Atendimento, Idoso_Dados

# Cria e lista os registros de atendimento
class AtendimentoListCreate(generics.ListCreateAPIView):
    serializer_class = AtendimentoSerializer

    def get_queryset(self):
        cpf = self.request.query_params.get('cpf')
        if cpf:
            return Atendimento.objects.filter(cpf_idoso__cpf=cpf)
        return Atendimento.objects.all()

    def post(self, request):
        cpf = request.data.get('cpf_idoso')
        if cpf:
            try:
                # Verificar se o idoso com o CPF fornecido existe
                idoso = Idoso_Dados.objects.get(cpf=cpf)
                request.data['cpf_idoso'] = idoso.cpf
                serializer = AtendimentoSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Idoso_Dados.DoesNotExist:
                return Response({"detail": "Idoso não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "CPF não fornecido."}, status=status.HTTP_400_BAD_REQUEST)

# Lista Resgatar atendimentos por cpf
class AtendimentoListByCPF(APIView):
    def get(self, request, format=None):
        """Retorna uma lista de atendimentos de um idoso específico baseado no CPF"""
        cpf = request.query_params.get('cpf')
        if cpf:
            atendimentos = Atendimento.objects.filter(cpf_idoso__cpf=cpf)
            if atendimentos.exists():
                serializer = AtendimentoSerializer(atendimentos, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Atendimentos não encontrados."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": "CPF não fornecido."}, status=status.HTTP_400_BAD_REQUEST)
