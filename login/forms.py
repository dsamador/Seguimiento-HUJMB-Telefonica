from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
  
  username = forms.CharField(
    label="Usuario",
    error_messages={
      "required": "Este campo es obligatorio.",      
    }
  )
  password = forms.PasswordInput(
    label="Usuario",
    error_messages={
      "required": "Este campo es obligatorio.",      
    }
  )

