from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	username = forms.CharField()
	nombre = forms.CharField()
	apellido = forms.CharField()
	#email =  forms.EmailField()
    #contrasena = models.CharField(max_length=50)