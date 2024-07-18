from django.urls import path
from .import views


urlpatterns = [

    path('Account/', views.AccountListCreate.as_view(), name='Account_List_Create'),
    path('Account/<int:pk>/', views.AccountRetrieveUpdateDestroy.as_view(), name='update'),
    path('login/', views.LoginView.as_view()),
 ]