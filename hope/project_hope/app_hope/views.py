from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Inicio(View):
    def get(self, request):
        return render(request, 'app_hope/index.html', {})

class Login(View):
    def get(self, request):
        return render(request, 'app_hope/login.html', {})

    def post(self, request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            print(request.user)
            return redirect('conta')
        else:
            error="Seu nome e/ou sua senha está(estão) incorreto(s)"
            return render(request,'app_hope/login.html', {'error':error})

class Cadastro(View):
    def get(self, request):
        return render(request, 'app_hope/cadastro.html', {})

    def post(self, request):
        username=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['pwd']
        tam = len(pwd)
        pwd2=request.POST['pwd2']
        usero = User.objects.filter(username=username)
        num=len(usero)
        error_name =None
        error_pass=None
        #teste (usuário já existente, tamanho da senha, senhas iguais)  
        if num==1 or tam<8 or pwd!=pwd2:
            if num==1:
                error_name="Por favor, escolha outro nome"
            if pwd!=pwd2:
                error_pass="As senhas não são iguais"
            return render(request,'app_hope/cadastro.html', {'error_name': error_name, 'error_pass':error_pass})
        else:    
            user=User.objects.create_user(username,email,pwd)
            user.save()
            return redirect('login')

class Conta(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        return render(request, 'app_hope/conta.html', {})
   

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')



