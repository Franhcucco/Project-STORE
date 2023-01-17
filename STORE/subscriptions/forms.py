from django import forms

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=50)
    mail = forms.CharField(max_length=100)
    