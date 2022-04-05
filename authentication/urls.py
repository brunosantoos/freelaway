from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.createUser, name="cadastro"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logout, name="logout")
]
