from django import forms

class RegistroTareas(forms.ModelForm):
    descripcion=forms.CharField(max_length=100)