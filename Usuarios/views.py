from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from Schedule.models import Data

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        if not nome.strip():
            print('O campo nome não poder ser nulo')
            return redirect('cadastro')
        if not email.strip():
            print('O campo email não poder ser nulo')
            return redirect('cadastro')
        if not senha.strip():
            print('O campo senha não poder ser nulo')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado!')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Email já cadastrado!')
            return redirect('cadastro')
        user= User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário Cadastrado com Sucesso!')
        return redirect('login')
    else:
       return render(request, 'Usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
         email = request.POST['email']
         senha = request.POST['senha']
         if email == "" or senha == "":
            messages.error(request, 'Os campos não podem ficar vazios')
            return redirect('login')
         print (email,senha)
         if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('agendar')
    return render(request, 'Usuarios/login.html')

def logout(request):
   auth.logout(request)
   return redirect('index')

def agendar(request):
    if request.method == 'POST':
        categoria = request.POST['categoria']
        profissional = request.POST['profissional']
        data = request.POST['data']
        user = get_object_or_404(User, pk=request.user.id)
        agenda = Data.objects.create(pessoa=user, categoria=categoria, profissional=profissional, data=data )
        agenda.save()
        return redirect('agendamentos')
    else:
        return render(request, 'Usuarios/agendar.html')

def agendamentos(request):
    if request.user.is_authenticated:
        return render(request, 'Usuarios/agendamentos.html')
    else:
        return redirect('index')
