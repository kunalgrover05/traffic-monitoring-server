from django import forms

class TrafficDataForm(forms.Form):
    file=forms.FileField()
