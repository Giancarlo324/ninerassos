from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Hojavida
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('stars_count', 'first_name', 'email', 'body')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control is-valid', 'placeholder': 'Nombres', 'readonly': 'True'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'True'}),
        }

    def clean_stars_count(self):
        stars_count = self.cleaned_data.get('stars_count')

        if stars_count < 0 or stars_count > 5:
            raise forms.ValidationError(
                "La calificación debe tener un rango de 0 a 5, por lo que "+str(stars_count)+" es incorrecto.")
        return stars_count


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
                raise forms.ValidationError(
                    "La identificación "+str(id)+" ya se encuentra registrada.")
        return id

    def clean_email(self):
        email = self.cleaned_data.get('email')

        for instance in User.objects.all():
            if instance.email == email:
                print("Ya esta registrada")
                raise forms.ValidationError(
                    "El email "+str(email)+" ya se encuentra registrado.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')

        for instance in User.objects.all():
            if instance.username == username:
                print("Ya esta registrada")
                raise forms.ValidationError(
                    "El usuario "+str(username)+" ya se encuentra registrado.")
        return username


class CambiarEstadoForm(forms.ModelForm):
    #username = UsernameField(widget = forms.TextInput(attrs = {'class': 'form-control form-control-sm'}))
    class Meta:
        model = User
        fields = ['ninera_disponible']


class ActualizarPerfilForm(forms.ModelForm):
    class Meta:
        model = Hojavida
        fields = ['imagen',
                  'title',
                  'content'
                  ]


class HojaVidaForm(forms.ModelForm):
    class Meta:
        model = Hojavida
        fields = ['imagen',
                  'id',
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
        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
            'id': forms.NumberInput(attrs={'class': 'form-control', 'id': 'hola', 'readonly': 'True'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control is-valid', 'placeholder': 'Nombres', 'readonly': 'True'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control is-valid', 'placeholder': 'Apellidos', 'readonly': 'True'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'num_telefono': forms.NumberInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'residencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Residencia'}),
            # 'habilidades': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Habilidades'}),
            # 'experiencia_lab': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Experiencia laboral'}),
            # 'formacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Formación académica'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre creativo de tu servicio'}),
            # 'content': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descríbete la manera en que brindas tu servicio'}),
        }

    def clean_num_telefono(self):
        num_telefono = self.cleaned_data.get('num_telefono')

        if len(str(num_telefono)) != 10:
            raise forms.ValidationError(
                "El número de celular "+str(num_telefono)+" es incorrecto.")
        return num_telefono
