from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import User

class BiodataForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            "username" : forms.TextInput(
                attrs={
                    'class': 'from-control',
                    'type': 'text',
                    'placeholder': 'User',
                    'required': True
                }),
            "email" : forms.Textarea(
                attrs={
                    'class': 'from-control',
                    'cols': '12',
                    'rows': '6',
                    'placeholder': 'Alamat',
                    'required': True
                }),
            # "telp" : forms.TextInput(
            #     attrs={
            #         'class': 'from-control',
            #         'type': 'text',
            #         'required': True
            #     }),
        }