from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Faz logout do usuario"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    """Faz cadastro de um novo usuario"""

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method != 'POST':
        #exibe um formulario em branco
        form = UserCreationForm()

    else:
        #processa o formulario preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz login do usuario e o  redireciona para a pagina inicial
            authenticated_user = authenticate(username=new_user.username, password= request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)