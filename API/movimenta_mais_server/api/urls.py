from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .auth import views_auth
from .Idoso_Atividades import views_atendimento, views_idoso, views_treino
from .Docs import views_exams

urlpatterns = [
    path('user_admin/', views_auth.User_AdminListCreate.as_view(), name="user_admin_list_create"),
    # Paths de Auth
    path('user_admin/<int:pk>/', views_auth.User_AdminRetrieveUpdateDestroy.as_view(), name="user_admin_retrieve_update_destroy"),
    path('user_admin/list/', views_auth.User_AdminList.as_view(), name='user_admin_list'),
    path('signin/', views_auth.sign_in, name='sign_in'),
    # Paths de Idoso_Atividades
    path('idosos_dados/cadastrar/', views_idoso.Idoso_DadosListCreate.as_view(), name="idoso_dados_cadastrar"),
    path('idosos_dados/<int:pk>/', views_idoso.Idoso_DadosRetrieveUpdateDestroy.as_view(), name="idoso_dados_retrieve_update_destroy"),
    path('idosos_dados/list/', views_idoso.Idoso_DadosList.as_view(), name='idosos_dados_list'),
    # Parte de Atendimento
    path('idosos_dados/atendimento/criar/', views_atendimento.AtendimentoListCreate.as_view(), name="idoso_atendimento_criar"),
    path('idosos_dados/atendimento/lista/', views_atendimento.AtendimentoListByCPF.as_view(), name="idoso_atendimento_lista"),
    # Treino
    path('idosos_dados/treino/create/', views_treino.TreinoCreateAPIView.as_view(), name='treino_create'),
    path('idosos_dados/treino/<int:pk>/', views_treino.TreinoRetrieverUpdateDestory.as_view(), name='treino_retrieve_update_destroy'),
    path('idosos_dados/treino/listar/', views_treino.TreinoList.as_view(), name='treino_listar'),
    # Paths de Docs
    path('docs/exame/upload', views_exams.upload_exame_view, name='upload_exame'),
    path('docs/exame/lista', views_exams.ExameListByCPF.as_view(), name='upload_lista'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
