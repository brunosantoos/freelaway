from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.


def createUser(request):
    if request.method == 'GET':
      if request.user.is_authenticated:
        return redirect('/')
      return render(request, 'sign.html')  
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        # validation password
        if not password == confirmPassword:
          messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
          return redirect('/auth/cadastro')
            

        if len(username.strip()) == 0 or len(password.strip()) == 0:
          messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
          return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)

        if user.exists():
          messages.add_message(request, constants.ERROR, 'Já existe um usário com esse username')
          return redirect('/auth/cadastro')

        try:
          user = User.objects.create_user(username=username, password=password)
          user.save()
          messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
          return redirect('/auth/login')

        except:
          messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
          return redirect('/auth/cadastro')  



def loginUser(request):
    if request.method == 'GET':
      if request.user.is_authenticated:
        return redirect('/')
      return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if not user:
          messages.add_message(request, constants.ERROR, 'Usuário ou senha incorreto')
          return redirect('/auth/login')
        else:
          auth.login(request, user)
          return redirect('/home/')



def logout(request):
  auth.logout(request)
  return redirect('/auth/login')       
