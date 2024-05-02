from django import forms

from .models import Product

class ProductRegister(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'company',  'tel', 'tel2', 'email', 'cnpj', 'headquarter', 'branch', 'maintenance')