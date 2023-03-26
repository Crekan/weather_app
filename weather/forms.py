from .models import City
from django import forms


class CityForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите город',
        'class': 'form-control',
        'id': 'city',
        'name': 'city',
    }))

    class Meta:
        model = City
        fields = ['name']
