from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Publish"))


class Hojavida(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    post = models.ForeignKey(Hojavida, on_delete=models.CASCADE, related_name="comments")
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