from django import forms
from .models import Categoria




class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    email = forms.EmailField(max_length=50, widget=forms.EmailInput())

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']