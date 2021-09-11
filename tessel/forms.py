from django import forms

class NameForm(forms.Form):
    username = forms.CharField(max_length = 100)
