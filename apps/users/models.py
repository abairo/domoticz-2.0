from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):    
    email = models.EmailField(_('Email'), unique=True)
    first_name = models.CharField(_('Nome'), max_length=50, blank=True)
    last_name = models.CharField(_('Sobrenome'), max_length=50, blank=True)
    birth_date = models.DateField(_('Data de nascimento'), null=True, blank=True)
    phone = models.CharField(_('Telefone'), max_length=15, null=True, blank=True)
    cpf = models.CharField(_('CPF'), max_length=15, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return '{}'.format(self.email)
