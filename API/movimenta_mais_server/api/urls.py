from django.urls import path
from .auth import views_auth
from .Idoso_Atividades import views_idoso

urlpatterns = [
    path('user_admin/',views_auth.User_AdminListCreate.as_view(), name="user_admin_list_create"),
    #Paths de Auth
    path('user_admin/<int:pk>/', views_auth.User_AdminRetrieveUpdateDestroy.as_view(), name="user_admin_retrieve_update_destroy"),
    path('user_admin/list/', views_auth.User_AdminList.as_view(), name='user_admin_list'),
    path('signin/', views_auth.sign_in, name='sing_in'),
    #Paths de Idoso_Atividades
    path('idosos_dados/cadastrar', views_idoso.Idoso_DadosListCreate.as_view(), name="idoso_dados_cadastrar"),
    path('idosos_dados/<int:pk>/', views_idoso.Idoso_DadosRetrieveUpdateDestroy.as_view(), name="idoso_dados_retrieve_update_destroy"),
    path('idosos_dados/list/', views_idoso.Idoso_DadosList.as_view(), name='idosos_dados_list'),
]

