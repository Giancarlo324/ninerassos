from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Hojavida
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class CustomUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']

    def clean_id(self):
        id = self.cleaned_data.get('id')
        
        for instance in User.objects.all():
            if instance.id == id:
                print("Ya esta registrada")
                raise forms.ValidationError("La identificación "+str(id)+" ya se encuentra registrada.")
        return id
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        for instance in User.objects.all():
            if instance.email == email:
                print("Ya esta registrada")
                raise forms.ValidationError("El email "+str(email)+" ya se encuentra registrado.")
        return email
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        for instance in User.objects.all():
            if instance.username == username:
                print("Ya esta registrada")
                raise forms.ValidationError("El usuario "+str(username)+" ya se encuentra registrado.")
        return username

class CambiarEstadoForm(forms.ModelForm):
    #username = UsernameField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-sm'}))
    class Meta:
        model = User
        fields = ['ninera_disponible']


class HojaVidaForm(forms.ModelForm):
    class Meta:
        model = Hojavida
        fields = ['id',
                  'first_name',
                  'last_name',
                  'birth_date',
                  'sex',
                  'email',
                  'num_telefono',
                  'residencia',
                  'habilidades',
                  'experiencia_lab',
                  'formacion',
                  'title',
                  'content']

    def clean_num_telefono(self):
        num_telefono = self.cleaned_data.get('num_telefono')
        
        if len(str(num_telefono)) != 10:
            raise forms.ValidationError("El número de celular "+str(num_telefono)+" es incorrecto.")
        return num_telefono
