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


class HojaVidaForm(forms.ModelForm):
    class Meta:
        model = Hojavida
        fields = ['id',
                  'first_name',
                  'last_name',
                  'birth_date',
                  'sex',
                  'email',
                  'title',
                  'content']
