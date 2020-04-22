from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from usuario.models import User
from datetime import datetime, timedelta


STATUS = ((0, "Draft"), (1, "Publish"))
SUSCRIPCION = ((0, "Finalizada"), (1, "Activa"))

# Una hoja de vida le pertenece a un usuario
# Una hoja de vida no puede existir sin un usuario
# OneToOneFiel

def now_plus_30():
    return datetime.now() + timedelta(days = 30)


class Hojavida(models.Model):
    imagen = models.ImageField("Foto de perfil", null=True, blank=True)
    id = models.IntegerField("Identificación", primary_key=True, unique=True)
    # Si un usuario se elimine, también se hará la relación hojavida
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    # con models.CASCADE
    # Se obliga a que hoja vida tenga relación con User.
    first_name = models.CharField("Nombres", max_length=255)
    last_name = models.CharField("Apellidos", max_length=255)
    birth_date = models.DateField("Fecha de nacimiento(mm/dd/yyyy)")
    SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    sex = models.CharField("Sexo", max_length=10, choices=SEX)
    email = models.EmailField("email", unique=True, max_length=255)
    num_telefono = models.IntegerField("Celular")
    residencia = models.CharField("Dirección de residencia", max_length=255)
    habilidades = models.TextField("Habilidades y aptitudes")
    experiencia_lab = models.TextField("Experiencia laboral")
    formacion = models.TextField("Formación académica")

    fecha_inicio = models.DateTimeField("Inicio de suscripción", auto_now_add=True)
    fecha_fin = models.DateTimeField("Fin de suscripción", default=now_plus_30)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    suscripcion = models.IntegerField(choices=SUSCRIPCION, default=0)
    """author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts"
    )"""

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(round(self.id*0.9+5))
        super(Hojavida, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    post = models.ForeignKey(
        Hojavida, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)


""" se crearán dos secciones, una para niñera y otra para cliente
todos van a ser usuarios en la sección de usuarios, pero cada uno
en el modelo será diferente, el modelo de niñera debe tener una
relación con el cliente que la contrate.
Se debe poner un identificador a los usuarios para identificar si
es niñera o es cliente, depende de eso al pulsar en el propio
perfil, se redirigirá a su propio modelo depende si es niñera
o cliente. """
