from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls), #Rota do site adm do Django
    path('api/',include("api.urls")), #Leva pra as rotas da API
    
]
