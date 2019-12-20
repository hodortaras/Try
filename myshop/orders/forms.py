from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'region', 'city', 'adress', 'coment']

        widgets={  'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'region': forms.TextInput(attrs={'class': 'form-control'}),
                   'city': forms.TextInput(attrs={'class': 'form-control'}),
                   'adress': forms.TextInput(attrs={'class': 'form-control'}),
                   'coment': forms.Textarea(attrs={'class': 'form-control'}),
        }
