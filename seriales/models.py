from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.

class Computador(models.Model):
  serial = models.CharField('SERIAL *', unique=True, max_length=10, blank=False, null=False, editable=False)
  mantenimiento_realizado = models.BooleanField(default=False)
  user = UserForeignKey(auto_user_add=True, auto_user=True)
  fecha_registro = models.DateField(auto_now=True)

  def save(self):
    self.serial = self.serial.upper()
    super(Computador, self).save()
  
  def __str__(self):
    return self.serial

