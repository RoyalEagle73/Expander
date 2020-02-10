from django import forms


class Data(forms.Form):
    name = forms.CharField(max_length=100)


