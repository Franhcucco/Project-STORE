from django import forms

class PantsForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    size = forms.IntegerField()
    stock = forms.BooleanField()
    pesos = '$'

class TshirtForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    size = forms.CharField(max_length=3)
    stock = forms.BooleanField()
    pesos = '$'

class ShoesForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    size = forms.IntegerField()
    stock = forms.BooleanField()
    pesos = '$'