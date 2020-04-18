from blog.forms import CustomUserForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate


# Create your views here.
def registrar_ninera(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            user.refresh_from_db()
            user.is_ninera = True
            user.save()
            # formulario.save()
            # Autenticar y redirigir al inicio o cambiar esto más adelante
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user =  authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, 'registration/registrarninera.html', data)
    

def registrar_cliente(request):
    
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            user.refresh_from_db()
            user.is_cliente = True
            user.save()
            # formulario.save()
            # Autenticar y redirigir al inicio o cambiar esto más adelante
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user =  authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')


    return render(request, 'registration/registrarcliente.html', data)


def profile_ninera(request):
    user = request.user
    hola = "ninera"

    if user.is_ninera:
        profile = user.get_ninera_profile()
        # Tal vez el doctor es nuevo y no tiene perfil
        if profile:
            print("Hola1")
            return render(request, 'profileninera.html', {
            "hola": hola
        })
        else:
            print("Hola2")
            return render(request, 'profileninera.html', {
            "hola": hola
        })
            # Redireccionar, levantar un error, etc.
    else:
        return render(request, '404.html')
        # Redireccionar, levantar un error, etc.


def profile_cliente(request):
    user = request.user
    hola = "clienteee"

    if user.is_cliente:
        profile = user.get_cliente_profile()
        # Tal vez el doctor es nuevo y no tiene perfil
        if profile:
            print("Hola1")
            return render(request, 'profilecliente.html', {
            "hola": hola
        })
            # Mas código
        else:
            print("Hola2")
            return render(request, 'profilecliente.html', {
            "hola": hola
        })
            # Redireccionar, levantar un error, etc.
    else:
        return render(request, '404.html')
        # Redireccionar, levantar un error, etc.
    

def crear_historia_clinica(request):
    user = request.user
    if user.is_ninera:
        profile = user.get_ninera_profile()
        # Tal vez el doctor es nuevo y no tiene perfil
        if profile:
            print("Hola1")
            # Mas código
        else:
            print("Hola2")
            # Redireccionar, levantar un error, etc.
    else:
        print("Hola3")
        # Redireccionar, levantar un error, etc.

def solo_para_clientes(request):
    user = request.user
    if user.groups.filter(name='cliente').exists():
        # Tiene los privilegios de este grupo
        print("hola")
    else:
        # Redireccionar, levantar un error, etc.
        print("hola")