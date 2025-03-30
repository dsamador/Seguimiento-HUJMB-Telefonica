from django.forms import ModelForm
from .models import Computador

class ComputadorForm(ModelForm):
  class Meta:
    model = Computador
    fields = ['serial']
    labels = {
      "serial": "Serial"
    }