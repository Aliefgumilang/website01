from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Daftar

class DaftarForms(forms.ModelForm):
    class Meta:
        model = Daftar
        fields = ('judul', 'deskripsi', 'kategori')
        widgets = {
            "judul" : forms.TextInput(
                attrs={
                    'class': 'from-control',
                    'type': 'text',
                    'placeholder': 'Judul',
                    'required': True
                }),
            "deskripsi" : forms.Textarea(
                attrs={
                    'class': 'from-control',
                    'cols': '12',
                    'rows': '6',
                    'placeholder': 'Deskripsi',
                    'required': True
                }),
            "kategori" : forms.Select(
                attrs={
                    'class': 'from-control',
                    'type': 'text',
                    'required': True
                }),
        }