from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from .forms import ExameForm  # Certifique-se de que o caminho está correto
from ..models import Exame 
from ..serializers import ExameSerializer


@csrf_exempt  # Para permitir requisições POST sem CSRF (apenas para exemplo; não recomendado em produção)
def upload_exame_view(request):
    if request.method == 'POST':
        form = ExameForm(request.POST, request.FILES)
        if form.is_valid():
            # Salvando o exame
            exame = form.save()

            # Retornando uma resposta JSON com os detalhes do exame salvo
            return JsonResponse({
                'status': 'success',
                'message': 'Exame salvo com sucesso!',
                'exame_id': exame.id,
                'cpf_idoso': exame.cpf_idoso.cpf,
                'title': exame.title,
                'uploaded_at': exame.uploaded_at.strftime('%Y-%m-%d %H:%M:%S'),
                'file_url': exame.file.url,
            })
        else:
            # Se o formulário não for válido, retornar uma resposta de erro com os erros do formulário
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        # Se não for uma requisição POST, retornar uma resposta de erro indicando que apenas POST é suportado
        return JsonResponse({'status': 'error', 'message': 'Apenas requisições POST são suportadas.'}, status=405)

#Lista Geral
class ExameList(APIView):
    def get(self, request, format=None):
        """Retorna uma lista de usuários"""
        nome = request.query_params.get("nome", "")
        
        if nome:
            users = Exame.objects.filter(nome__icontains=nome)
        else:
            users = Exame.objects.all()
            
        serializer = ExameSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Lista Resgatar Exames por cpf
class ExameListByCPF(APIView):
    def get(self, request, format=None):
        """Retorna uma lista de Exames de um idoso específico baseado no CPF"""
        cpf = request.query_params.get('cpf')
        if cpf:
            Exames = Exame.objects.filter(cpf=cpf)
            if Exames.exists():
                serializer = ExameSerializer(Exames, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Exames não encontrados."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": "CPF não fornecido."}, status=status.HTTP_400_BAD_REQUEST)


#Apaga File escolhido
@api_view(['DELETE'])
def delete(request):
    title = request.query_params.get('title')
    if title:
        try:
            exame = get_object_or_404(Exame, title=title)  # Fetch the exam object based on title
            exame.delete()
            return Response({"message": "Exame deletado com sucesso"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "title não fornecido"}, status=status.HTTP_400_BAD_REQUEST)        
        
    