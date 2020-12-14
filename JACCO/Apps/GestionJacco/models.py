from django.db import models

# Create your models here.

class cliente (models.Model):

	Apellido = models.CharField(max_length=35)
	Nombre = models.CharField(max_length=35)
	DNI = models.CharField(max_length=35)
	RUC = models.CharField(max_length=35)

	def NombreCompleto (self):
		cadena = "{} {} ".format (self.Apellido, self.Nombre) 
		return cadena
	def __str__(self):
		return self.NombreCompleto ()

class registro (models.Model):

	cliente = models.ForeignKey (cliente, null=False, blank=False, on_delete=models.CASCADE)
	FechaRegistro = models.DateTimeField (auto_now_add=True)

	def __str__(self):
		cadena = "{0} => {1}".format (self.cliente)
		return cadena
