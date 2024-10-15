from django.urls import path
from .import views


urlpatterns = [

    path('Account/', views.Account_list_create.as_view(), name='Account_List_Create'),
    path('Account/<int:pk>/', views.Account_retrieve_update_destroy.as_view(), name='update'),
    path('login/', views.Login_view.as_view()),
 ]