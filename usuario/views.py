from blog.forms import CustomUserForm, HojaVidaForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import User
from blog.models import Hojavida


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
            user.ninera_disponible = True
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
    new_hoja_vida = None
    user = request.user
    hola = "ninera"
    usuario = User.objects.get(id = user.id)


    if user.is_ninera:
        profile = user.get_ninera_profile()
        # Tal vez la niñera es nueva y no tiene perfil
        if profile:
            print("Hola1")
            data = {
                'form':HojaVidaForm()
            }
            if request.method == 'POST':
                formulario = HojaVidaForm(request.POST)
                if formulario.is_valid():
                    formulario.save()
                    data['mensaje'] = "Registrado correctamente"
            return render(request, 'profileninera.html', data)
        else:
            print("Hola2")
            print("Hola2"+str(user.id))
            data = {
                'form':HojaVidaForm(instance=usuario)
            }
            if request.method == 'POST':
                formulario = HojaVidaForm(request.POST)
                if formulario.is_valid():
                    # Actualizar a que ya tiene hoja de vida
                    actualizacion = User.objects.get(id = user.id)
                    User.objects.filter(pk=user.id).update(tiene_hoja_vida=True)
                    actualizacion.refresh_from_db()
                    # Guardar
                    """hoja_vida = formulario.save()
                    hoja_vida.refresh_from_db()
                    hoja_vida.usuario = Hojavida.objects.get(id=user.id)"""
                    # hoja_vida.usuario = user
                    # hoja_vida.save()
                    formulario.save()
                    data['mensaje'] = "Registrado correctamente"
                    return redirect(to='home')

            return render(request, 'profileninera.html', data)
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