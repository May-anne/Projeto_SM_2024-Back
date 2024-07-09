from django.urls import path
from .auth import views

urlpatterns = [
    path('user_admin/', views.User_AdminListCreate.as_view(), name="user_admin_list_create"),
    path('user_admin/<int:pk>/', views.User_AdminRetrieveUpdateDestroy.as_view(), name="user_admin_retrieve_update_destroy"),
    path('user_admin/list/', views.User_AdminList.as_view(), name='user_admin_list'),
    path('signin/', views.sign_in, name='sing_in'),
]
