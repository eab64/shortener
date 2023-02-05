from django import forms

class UrlForm(forms.Form):
    url = forms.CharField(label='your url', max_length=255)