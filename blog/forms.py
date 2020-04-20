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
