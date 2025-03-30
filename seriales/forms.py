from django.forms import ModelForm
from .models import Computador
from django import forms

class ComputadorForm(forms.ModelForm):
  
  serial = forms.CharField(
    label="Serial",
    error_messages={
      "required": "Este campo es obligatorio.",
      "unique": "Ya existe un computador con este serial.",
      "max_length": "El serial no puede tener más de 10 caracteres."
    }
  )

  class Meta:
    model = Computador
    fields = ['serial']        