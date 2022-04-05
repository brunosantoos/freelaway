from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.http import HttpResponse

# Create your views here.


def createUser(request):
    if request.method == 'GET':
        return render(request, 'sign.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        # validation password
        if not password == confirmPassword:
            return redirect('/auth/cadastro')

        if len(username.strip()) > 0 or len(password.strip()) > 0:
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)

        if user.exist():
          return redirect('/auth/cadastro')

        return HttpResponse("Recebido")


def loginUser(request):
    return HttpResponse('Login')
