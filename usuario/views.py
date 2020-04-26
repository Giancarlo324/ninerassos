from blog.forms import CustomUserForm, HojaVidaForm, CambiarEstadoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import User
from blog.models import Hojavida
from datetime import datetime, timedelta


# Create your views here.
def registrar_ninera(request):
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            user.refresh_from_db()
            user.is_ninera = True
            user.ninera_disponible = False
            user.save()
            # formulario.save()
            # Autenticar y redirigir al inicio o cambiar esto más adelante
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='profile_ninera')
    else:
        formulario = CustomUserForm()

    data = {
        'form': formulario
    }
    return render(request, 'registration/registrarninera.html', data)


def registrar_cliente(request):
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
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
    else:
        formulario = CustomUserForm()

    data = {
        'form': formulario
    }
    return render(request, 'registration/registrarcliente.html', data)

@login_required
def profile_ninera(request):
    new_hoja_vida = None
    user = request.user
    hola = "ninera"
    usuario = User.objects.get(id=user.id)

    if user.is_ninera:
        profile = user.get_ninera_profile()
        # Tal vez la niñera es nueva y no tiene perfil
        if profile:
            print("Hola1")
            data = {
                'form': HojaVidaForm()
            }
            if request.method == 'POST':
                formulario = HojaVidaForm(request.POST)
                if formulario.is_valid():
                    formulario.save()
                    data['mensaje'] = "Registrado correctamente"
                else:
                    data['mensaje'] = "Ocurrió un error"
            return render(request, 'profileninera.html', data)
        else:
            print("Hola2")
            print("Hola2"+str(user.id))
            #
            # Si está disponible, es porque ya llenó la hoja de vida
            if user.tiene_hoja_vida:
                post = Hojavida.objects.get(id=user.id)
                data = {'form': CambiarEstadoForm(instance=usuario), 'post':post,}
                if request.method == 'POST':
                    formulario = CambiarEstadoForm(
                        request.POST, instance=request.user)
                    if formulario.is_valid():
                        modificar_estado = formulario.save(commit=False)
                        modificar_estado.save()
                        # actualizacion = User.objects.get(id = user.id)
                        # formulario.save()
                        data['mensaje'] = "Registrado correctamente"
                        return redirect(to='profile_ninera')
                    else:
                        data['mensaje'] = "Ocurrió un error"
                return render(request, 'profileninera.html', data)
            else: # No tiene hoja de vida
                
                if request.method == 'POST':
                    formulario = HojaVidaForm(request.POST, files=request.FILES)
                    if formulario.is_valid():
                        # Actualizar a que ya tiene hoja de vida y ninera disponible
                        actualizacion = User.objects.get(id=user.id)
                        User.objects.filter(pk=user.id).update(
                            tiene_hoja_vida=True)
                        User.objects.filter(pk=user.id).update(
                            ninera_disponible=True)
                        actualizacion.refresh_from_db()
                        # Guardar
                        hoja_vida = formulario.save(commit=False)
                        hoja_vida.usuario = User.objects.get(id=user.id)
                        hoja_vida.save()
                        return redirect(to='home')
                else:
                    formulario = HojaVidaForm(instance=usuario)
                
                data = {
                    'form': formulario
                }

                return render(request, 'profileninera.html', data)
                # Redireccionar, levantar un error, etc.
    else:
        return render(request, '404.html')
        # Redireccionar, levantar un error, etc

@login_required
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
