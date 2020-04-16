from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_ninera = models.BooleanField(default=False)
    is_cliente = models.BooleanField(default=False)

    def get_ninera_profile(self):
        ninera_profile = None
        if hasattr(self, 'nineraprofile'):
            ninera_profile = self.nineraprofile
        return ninera_profile

    def get_cliente_profile(self):
        cliente_profile = None
        if hasattr(self, 'clienteprofile'):
            cliente_profile = self.clienteprofile
        return cliente_profile

    class Meta:
        db_table = 'auth_user'

class NineraProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)


class ClienteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)