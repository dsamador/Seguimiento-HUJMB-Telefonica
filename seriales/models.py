from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.

class Computador(models.Model):
  serial = models.CharField('SERIAL *', unique=True, max_length=10, blank=False, null=False,)
  mantenimiento_realizado = models.BooleanField(default=False)
  user = UserForeignKey(auto_user_add=True, auto_user=True)
  fecha_registro = models.DateField(auto_now=True)
  fecha_modificacion = models.DateTimeField(auto_now_add=True)

  def save(self, *args, **kwargs):
    self.serial = self.serial.upper()
    super(Computador, self).save(*args, **kwargs)
  
  def __str__(self):
    estado = "Sí" if self.mantenimiento_realizado else "No"
    return f"{self.serial} | Mantenimiento: {estado}"


