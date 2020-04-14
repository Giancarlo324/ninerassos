from django.contrib.auth.forms import UserCreationForm
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class CustomUserForm(UserCreationForm):
    pass