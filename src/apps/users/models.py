from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from .managers import *

class PerfilQuerySet(models.QuerySet):
	def capacitadores(self):
		return self.filter(user__groups__in="Capacitación")

class PerfilManager(models.Manager):
	def get_queryset(self):
		return PerfilQuerySet(self.model, using=self._db)

	def capacitadores(self):
		return self.get_queryset.capacitadores()

class Perfil(models.Model):
	GENERO_CHOICES = (
		('M', 'Masculino'),
		('F', 'Femenino'),
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dpi = models.CharField(max_length=20, unique=True)
	public = models.BooleanField(default=True)
	genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default='M')
	fecha_nacimiento = models.DateField(null=True, blank=True)
	direccion = models.CharField(max_length=150, null=True, blank=True)
	foto = ThumbnailerImageField(
		upload_to="perfil_usuario",
        null=True,
        blank=True,
        editable=True,
		)
	objects = models.Manager()
	grupos = PerfilManager.from_queryset(PerfilQuerySet)()
	
	def get_nombre(self):
		return self.user.first_name
	nombre = property(get_nombre)

	def get_apellido(self):
		return self.user.last_name
	apellido = property(get_apellido)


	def get_absolute_url(self):
		return reverse('perfil_detail', kwargs={'pk':self.id})

	class Meta:
		verbose_name = 'perfil'
		verbose_name_plural = 'perfiles'

	def __str__(self):
		return self.nombre + " " + self.apellido

class PerfilTelefono(models.Model):
	perfil = models.ForeignKey(Perfil)
	numero = models.CharField(max_length=10)
	principal = models.BooleanField(default=False)

	objects = TelefonoManager()

	class Meta:
		verbose_name = "Teléfono de perfil"
		verbose_name_plural = "Teléfonos de perfil"

	def __str__(self):
		return self.numero